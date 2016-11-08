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

# Extension class so can't be supported
# import datetime
# defineChecker(datetime, NamesChecker([meth for meth in dir(datetime) if meth[0] != '_']))
# allow_module('datetime')
# allow_class(datetime.datetime)

#defineChecker(time, NamesChecker([meth for meth in dir(time) if meth[0] != '_']))
#allow_module('time')


# Itertools
allow_module('itertools')


# CSV

allow_module('csv')
import csv
allow_class(csv.DictReader)
allow_class(csv.DictWriter)
allow_class(csv.Dialect)
allow_class(csv.excel)
allow_class(csv.excel_tab)
allow_class(csv.Sniffer)


# StringIO

allow_module('StringIO')
import StringIO
allow_class(StringIO.StringIO)

allow_module('cStringIO')
