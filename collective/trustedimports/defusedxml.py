from AccessControl import ModuleSecurityInfo

import defusedxml

ModuleSecurityInfo('defusedxml.lxml').declarePublic('fromstring')
ModuleSecurityInfo('defusedxml.lxml').declarePublic('parse')


