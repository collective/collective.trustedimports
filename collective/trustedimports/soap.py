from collective.trustedimports.util import whitelist_module, wrap_protected, is_url_allowed
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zeep import Client
from zeep.proxy import ServiceProxy
from zeep.exceptions import Error
from zeep.transports import Transport

def is_transport_allowed(**kwargs):
    if 'transport' in kwargs:
        return False
    return True

def client_allowed(wsdl,**kwargs):
    return is_transport_allowed(**kwargs) and is_url_allowed(wsdl)

# monkey patching zeep
wrap_protected(Client.__init__, client_allowed)
wrap_protected(Client.bind)
wrap_protected(Client.create_service)

allow_class(Client)
# Require for client.service to work
allow_class(Transport)
allow_class(ServiceProxy)
allow_class(Error)

ModuleSecurityInfo('zeep').declarePublic('Client')
ModuleSecurityInfo('zeep.exceptions').declarePublic('Error')
ModuleSecurityInfo('zeep.transports').declarePublic('Transport')