from collective.trustedimports.util import whitelist_module, wrap_protected, is_url_allowed
import os
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from suds.client import Client
from suds import WebFault
from suds import MethodNotFound
import re
import fnmatch

def is_transport_allowed(transport=None):
    if transport:
        return False
    return True

def client_allowed(url=None, uri=None, link=None,transport=None):
    return is_transport_allowed(transport) and is_url_allowed(url, uri, link)

# monkey patching zipfile
wrap_protected(Client.__init__, client_allowed)
wrap_protected(Client.set_options, is_transport_allowed)

ModuleSecurityInfo('collective.trustedimports.suds').declarePublic('SafeClient')

allow_class(Client)
ModuleSecurityInfo('suds').declarePublic('WebFault','MethodNotFound')

allow_class(WebFault)
allow_class(MethodNotFound)

