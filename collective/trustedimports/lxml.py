from AccessControl import ModuleSecurityInfo

import lxml

def lxml_xpath(element, xpath, namespaces={}):
    """Helper method to use lxml xpath

    TODO: need to remove it when we know how to make the real api work
    problem is that cpython can't have security declarations?
    """

    if namespaces:
        result = element.xpath(xpath, namespaces=namespaces)
    else:
        result = element.xpath(xpath)
    return result

ModuleSecurityInfo("collective.trustedimports.lxml").declarePublic(
    "lxml_xpath")
