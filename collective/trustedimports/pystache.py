from AccessControl import ModuleSecurityInfo

try:
    import pystache
except ImportError:
    pystache = None

if pystache is not None:
    ModuleSecurityInfo('pystache').declarePublic('render')
