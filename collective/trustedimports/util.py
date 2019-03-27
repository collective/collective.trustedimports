import importlib
import os
from AccessControl import allow_type
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zope.security.checker import defineChecker, CheckerPublic, NamesChecker, selectChecker
import inspect
from collections import OrderedDict
import itertools
import re
import fnmatch

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

def restricted_python_call():
    # HACK: must be a better way to do this
    caller = inspect.stack()[2][1]
    return caller == 'Script (Python)'



def is_url_allowed(url=None, uri=None, link=None):
    blacklist = os.getenv('SAFEIMPORTS_URL_BLACKLIST', '')
    # Use semicolin delimiter for multiple url in blacklist
    blacklist = ["*%s*" % domain.strip() for domain in blacklist.split(';') if domain.strip()]
    if not blacklist:
        return True
    urls = [name for name in [url,uri,link] if name is not None]
    for pattern in blacklist:
        for url in urls:
            if fnmatch.fnmatch(url, pattern):
                raise ValueError("URL %s is not allowed to be accessed" % url)
    return True

def wrap_protected(method, *is_alloweds):
    """
    Will wrap a method in a way that will raise an exception of the test fails and this method was
    called directly from restricted python.
    `is_allowed` can be a callable taking arguments from the original methods arguments
    """

    if not inspect.ismethod(method):
        raise ValueError("method must be a method")
    if method.__name__ == 'not_allowed':
        # don't mokey patch twice
        return

    klass = method.im_class

    original = getattr(klass, method.__name__)
    if not is_alloweds:
        def not_allowed(*args, **kwargs):
            if restricted_python_call():
                # TODO: change to a better exception
                raise ValueError("Method '%s' not supported in a restricted python call"%method.__name__)
            return original.__call__(*args, **kwargs)

    else:
        names, args_name, kwargs_name, defaults = inspect.getargspec(method)
        def not_allowed(*args, **kwargs):
            args_name = list(OrderedDict.fromkeys(names + kwargs.keys()))
            args_dict = OrderedDict(list(itertools.izip(args_name, args)) + list(kwargs.iteritems()))
            if restricted_python_call():
                for is_allowed in is_alloweds:
                    seeking, _, _, _ = inspect.getargspec(is_allowed)
                    if not any([s in args_dict for s in seeking]):
                        continue
                    if not is_allowed(**dict([(s,args_dict[s]) for s in seeking])):
                        found = ','.join(seeking)
                        raise ValueError("Argument(s) '%s' have values not supported in a restricted python call"%found)
            return original.__call__(*args, **kwargs)


    not_allowed.__name__ = method.__name__
    setattr(klass, method.__name__, not_allowed)
