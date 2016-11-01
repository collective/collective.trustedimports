from Products.PythonScripts.tests.testPythonScript import VerifiedPythonScript, readf
from zope.untrustedpython import interpreter, rcompile
from zope.untrustedpython.builtins import SafeBuiltins

from Products.PythonScripts.PythonScript import PythonScript
from AccessControl.SecurityManagement import newSecurityManager
from AccessControl.SecurityManagement import noSecurityManager
from RestrictedPython.tests.verify import verify
from zope.component import eventtesting
from zope.component import provideAdapter
from zope.component import testing
from zope.interface import Interface
import doctest
import unittest

_ms_before = None
_ams_before = None

def setUp(test=None):
    testing.setUp()

    # PythonScripts
    from AccessControl import ModuleSecurityInfo as MSI
    from AccessControl.SecurityInfo import _moduleSecurity
    from AccessControl.SecurityInfo import _appliedModuleSecurity
    _ms_before = _moduleSecurity.copy()
    _ams_before = _appliedModuleSecurity.copy()
    MSI('string').declarePublic('split')
    MSI('sets').declarePublic('Set')
    newSecurityManager(None, None)

def teardown(test=None):
    testing.tearDown()

    # PythonScripts
    from AccessControl.SecurityInfo import _moduleSecurity
    from AccessControl.SecurityInfo import _appliedModuleSecurity
    noSecurityManager()
    _moduleSecurity.clear()
    _moduleSecurity.update(_ms_before)
    _appliedModuleSecurity.clear()
    _appliedModuleSecurity.update(_ams_before)



class Test_Interpreter(unittest.TestCase):

    def test_simple(self):
        d = {}
        interpreter.exec_src("x=1", d)
        self.assertEqual(d['x'], 1)
        self.assertEqual(d['__builtins__'], SafeBuiltins)

    def test_proxied(self):
        d = {}
        interpreter.exec_src('str=str', d)
        from zope.security.proxy import Proxy
        self.assertEqual(type(d['str']), Proxy)

    def test_no_builtins_mutations(self):
        from zope.security.interfaces import ForbiddenAttribute
        d = {}
        interpreter.exec_src("x=1", d)
        self.assertRaises(
            ForbiddenAttribute, interpreter.exec_src,
            '__builtins__.__dict__["x"] = 1', d)
        self.assertRaises(
            ForbiddenAttribute, interpreter.exec_src,
            'del __builtins__.__dict__["str"]', d)
        self.assertRaises(
            ForbiddenAttribute, interpreter.exec_src,
            '__builtins__.__dict__.update({"x": 1})', d)

    def test_no_exec(self):
        d = {}
        self.assertRaises(SyntaxError, interpreter.exec_src, "exec 'x=1'", d)

    def test_exec_code(self):
        d = {}
        code = compile('x=2', '<mycode>', 'exec')
        interpreter.exec_code(code, d)
        self.assertEqual(d['x'], 2)


class PythonScriptTestBase(unittest.TestCase):
    def setUp(self):
        from AccessControl import ModuleSecurityInfo as MSI
        from AccessControl.SecurityInfo import _moduleSecurity
        from AccessControl.SecurityInfo import _appliedModuleSecurity
        self._ms_before = _moduleSecurity.copy()
        self._ams_before = _appliedModuleSecurity.copy()
        MSI('string').declarePublic('split')
        MSI('sets').declarePublic('Set')
        newSecurityManager(None, None)

    def tearDown(self):
        from AccessControl.SecurityInfo import _moduleSecurity
        from AccessControl.SecurityInfo import _appliedModuleSecurity
        noSecurityManager()
        _moduleSecurity.clear()
        _moduleSecurity.update(self._ms_before)
        _appliedModuleSecurity.clear()
        _appliedModuleSecurity.update(self._ams_before)

    def _newPS(self, txt, bind=None):
        ps = VerifiedPythonScript('ps')
        ps.ZBindings_edit(bind or {})
        ps.write(txt)
        ps._makeFunction()
        if ps.errors:
            raise SyntaxError, ps.errors[0]
        return ps

    def _filePS(self, fname, bind=None):
        ps = VerifiedPythonScript(fname)
        ps.ZBindings_edit(bind or {})
        ps.write(readf(fname))
        ps._makeFunction()
        if ps.errors:
            raise SyntaxError, ps.errors[0]
        return ps

class TestPythonScriptNoAq(PythonScriptTestBase):

    def testEmpty(self):
        empty = self._newPS('')()
        self.failUnless(empty is None)

    def testIndented(self):
        # This failed to compile in Zope 2.4.0b2.
        res = self._newPS('if 1:\n return 2')()
        self.assertEqual(res, 2)

    def testReturn(self):
        res = self._newPS('return 1')()
        self.assertEqual(res, 1)

    def testReturnNone(self):
        res = self._newPS('return')()
        self.failUnless(res is None)

    def testParam1(self):
        res = self._newPS('##parameters=x\nreturn x')('txt')
        self.assertEqual(res, 'txt')


def teval(txt, bind=None):
    ps = VerifiedPythonScript('ps')
    ps.ZBindings_edit(bind or {})
    ps.write(txt)
    ps._makeFunction()
    if ps.errors:
        raise SyntaxError, ps.errors[0]
    return ps()


def test_suite():
    return unittest.TestSuite([
        doctest.DocFileSuite(
            'zip.rst',
            package='collective.trustedimports',
            optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
            setUp=setUp,
            tearDown=testing.tearDown,
            globs=dict(teval=teval),
        ),
    ])
