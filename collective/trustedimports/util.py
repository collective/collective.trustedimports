from AccessControl import allow_type
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zope.security.checker import defineChecker, CheckerPublic, NamesChecker



def whitelist_module(module, classes=[], definitions=[]):

    # For python scripts and zope
    allow_module(module)
    for klass in classes:
        allow_class(klass)
    if definitions:
        ModuleSecurityInfo(module).declarePublic(*definitions)

    # for zope.untrustedpython
    defineChecker(imodule,
                  NamesChecker([meth for meth in dir(imodule) if meth[0] != '_']))
