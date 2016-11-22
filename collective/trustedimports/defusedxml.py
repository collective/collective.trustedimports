from AccessControl import ModuleSecurityInfo
from AccessControl import allow_class

try:
    import defusedxml
except ImportError:
    defusedxml = None

if defusedxml is not None:
    ModuleSecurityInfo('defusedxml.ElementTree').declarePublic('fromstring')
    ModuleSecurityInfo('defusedxml.ElementTree').declarePublic('parse')

try:
    import xml
except ImportError:
    xml = None

if xml is not None:
    allow_class(xml.etree.ElementTree.ElementTree)
    ModuleSecurityInfo('xml.etree.ElementTree.ElementTree').declarePublic(
        'getroot')
    allow_class(xml.etree.ElementTree.Element)
    ModuleSecurityInfo('xml.etree.ElementTree.Element').declarePublic(
        'findall')
