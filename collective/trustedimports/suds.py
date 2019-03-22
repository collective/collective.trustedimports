from collective.trustedimports.util import whitelist_module
import os
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from suds.client import Client as _Client
from suds import WebFault
from suds import MethodNotFound


class SafeClient(_Client):
    """ SafeClient
    """

    def __init__(self, url, **kwargs):

        blacklist = os.getenv('SAFEIMPORTS_URL_BLACKLIST ', '')
        if url in blacklist:
            raise Unauthorized("Not supported by SafeClient in this context")

        return _Client.__init__(self, url, kwargs)


# monkey patching zipfile
suds.client.Client = SafeClient

ModuleSecurityInfo('collective.trustedimports.suds').declarePublic('SafeClient')

allow_class(SafeClient)
ModuleSecurityInfo('suds').declarePublic('WebFault','MethodNotFound')

allow_class(WebFault)
allow_class(MethodNotFound)