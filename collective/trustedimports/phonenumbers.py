from AccessControl import ModuleSecurityInfo
from Products.PythonScripts.Utility import allow_module
from collective.trustedimports.util import whitelist_module

import phonenumbers
ModuleSecurityInfo('phonenumbers').declarePublic('render')
whitelist_module('phonenumbers', [], ['country_code_for_region'])
