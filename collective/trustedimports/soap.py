from collective.trustedimports.util import whitelist_module, wrap_protected, is_url_allowed
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zeep import Client
from zeep.proxy import ServiceProxy


def is_transport_allowed(**kwargs):
    if 'settings' in kwargs:
        setting = kwargs['settings']
        if 'force_https' in setting or getattr(setting,'force_https',None):
            return False
        if 'extra_http_headers' in setting or getattr(setting,'extra_http_headers',None):
            return False
    return True

def client_allowed(wsdl,**kwargs):
    return is_transport_allowed(**kwargs) and is_url_allowed(wsdl)

# monkey patching suds
wrap_protected(Client.__init__, client_allowed)
wrap_protected(Client.bind)
wrap_protected(Client.create_service)

ModuleSecurityInfo('zeep').declarePublic('Client')
allow_class(Client)
allow_class(ServiceProxy)