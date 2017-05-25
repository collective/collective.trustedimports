import importlib
from AccessControl import allow_type
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zope.security.checker import defineChecker, CheckerPublic, NamesChecker, selectChecker


def whitelist_module(module, classes=[], definitions=[]):

    imodule = importlib.import_module(module)

    # For python scripts and zope
    if definitions:
        ModuleSecurityInfo(module).declarePublic(*definitions)
    else:
        allow_module(module)
    for klass in classes:
        allow_class(getattr(imodule, klass))

    # for zope.untrustedpython
    if not definitions:
        definitions = dir(module)


    if selectChecker(imodule) is None:
        defineChecker(imodule,
                  NamesChecker([meth for meth in definitions if meth[0] != '_']))
    #TODO classes
