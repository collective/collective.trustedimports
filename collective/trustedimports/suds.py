from collective.trustedimports.util import whitelist_module, wrap_protected, is_url_allowed
import suds
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from suds.client import Client as SafeClient
from suds import WebFault
from suds import MethodNotFound


def is_transport_allowed(transport=None):
    if transport:
        return False
    return True

def client_allowed(url=None, uri=None, link=None,transport=None):
    return is_transport_allowed(transport) and is_url_allowed(url, uri, link)

# monkey patching zipfile
wrap_protected(SafeClient.__init__, client_allowed)
wrap_protected(SafeClient.set_options, is_transport_allowed)

ModuleSecurityInfo('suds').declarePublic('Client')

allow_class(SafeClient)
ModuleSecurityInfo('suds').declarePublic('WebFault','MethodNotFound')

allow_class(WebFault)
allow_class(MethodNotFound)

