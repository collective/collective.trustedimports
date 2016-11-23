from AccessControl import ModuleSecurityInfo

try:
    import defusedxml
except ImportError:
    defusedxml = None

if defusedxml is not None:
    ModuleSecurityInfo('defusedxml.lxml').declarePublic('fromstring')
    ModuleSecurityInfo('defusedxml.lxml').declarePublic('parse')

try:
    import lxml
except ImportError:
    lxml = None


def lxml_xpath(element, xpath, namespaces={}):
    """Helper method to use lxml xpath

    TODO: need to remove it when we know how to make the real api work
    """
    if lxml is None:
        raise ImportError('lxml is not found.')

    if namespaces:
        result = element.xpath(xpath, namespaces=namespaces)
    else:
        result = element.xpath(xpath)
    return result

ModuleSecurityInfo("collective.trustedimports.defusedxml").declarePublic(
    "lxml_xpath")
