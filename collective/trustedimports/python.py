from AccessControl import allow_type
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zope.security.checker import defineChecker, CheckerPublic, NamesChecker

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
#z3
import random
#defineChecker(random, NamesChecker(['uniform','shuffle']))
defineChecker(random, NamesChecker([meth for meth in dir(random) if meth[0] != '_']))
import time, datetime
defineChecker(time, NamesChecker([meth for meth in dir(time) if meth[0] != '_']))
defineChecker(datetime, NamesChecker([meth for meth in dir(datetime) if meth[0] != '_']))



# Itertools
allow_module('itertools')