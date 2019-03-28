from collective.trustedimports.util import whitelist_module, wrap_protected, is_url_allowed
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zeep import Client
from zeep.proxy import ServiceProxy
from zeep.exceptions import Error
from zeep.transports import Transport


# monkey patching zeep
wrap_protected(Client.__init__, lambda transport: False, lambda wsdl: is_url_allowed(wsdl))
wrap_protected(Client.create_service, lambda address: is_url_allowed(address))

allow_class(Client)
# Require for client.service to work
allow_class(ServiceProxy)
allow_class(Error)

ModuleSecurityInfo('zeep').declarePublic('Client')
ModuleSecurityInfo('zeep.exceptions').declarePublic('Error')
