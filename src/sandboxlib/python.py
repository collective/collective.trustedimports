from AccessControl import allow_type
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module

# Basic python libs




# Allow RE in restricted python. Based on collective.localfunctions
# by Steve McMahon
import re
allow_module('re')
ModuleSecurityInfo('re').declarePublic(
    'compile', 'findall', 'match', 'search', 'split', 'sub', 'subn', 'error',
    'I', 'L', 'M', 'S', 'X')
allow_type(type(re.compile('')))
allow_type(type(re.match('x', 'x')))


# Random

allow_module('random')

# Itertools
allow_module('itertools')