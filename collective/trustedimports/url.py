from collective.trustedimports.util import whitelist_module, wrap_protected, is_url_allowed
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
import urllib
import urlparse

ModuleSecurityInfo('urllib').declarePublic('quote')
ModuleSecurityInfo('urlparse').declarePublic('urlparse')
ModuleSecurityInfo('urlparse').declarePublic('urljoin')

import requests
ModuleSecurityInfo('requests').declarePublic('get')
ModuleSecurityInfo('requests').declarePublic('post')
allow_class(requests.models.Response)
