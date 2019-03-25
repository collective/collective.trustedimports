from collective.trustedimports.util import whitelist_module, wrap_protected, is_url_allowed
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from suds.client import Client
from suds import WebFault, MethodNotFound
from suds.transport.https import HttpAuthenticated

def is_transport_allowed(**kwargs):
    if 'transport' in kwargs:
        return False
    return True

def client_allowed(url,**kwargs):
    return is_transport_allowed(**kwargs) and is_url_allowed(url)

# monkey patching suds
wrap_protected(Client.__init__, client_allowed)
wrap_protected(Client.set_options, is_transport_allowed)

ModuleSecurityInfo('suds.client').declarePublic('Client')
allow_class(Client)
ModuleSecurityInfo('suds.transport.https').declarePublic('HttpAuthenticated')
allow_class(HttpAuthenticated)

ModuleSecurityInfo('suds').declarePublic('WebFault','MethodNotFound')

allow_class(WebFault)
allow_class(MethodNotFound)

