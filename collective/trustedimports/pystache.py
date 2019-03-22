from AccessControl import ModuleSecurityInfo

import pystache

ModuleSecurityInfo('pystache').declarePublic('render')
