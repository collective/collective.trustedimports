# Basic ZODB stuff
import persistent.list
import persistent.dict
from AccessControl import ModuleSecurityInfo

from zope.security.checker import defineChecker, NamesChecker

defineChecker(persistent.list, NamesChecker(['PersistentList']))
defineChecker(persistent.dict, NamesChecker(['PersistentDict']))

dict_checker = NamesChecker(['__call__','__init__','__getitem__', '__len__', '__iter__',
                        'get', 'has_key', 'copy', '__str__', 'keys',
                        'values', 'items', 'iterkeys', 'iteritems',
                        'itervalues', '__contains__'])
persistent.dict.PersistentDict.__Security_checker__ = dict_checker
list_checker = NamesChecker(['__call__','__init__','__getitem__', '__getslice__', '__len__', '__iter__',
                        '__contains__', 'index', 'count', '__str__',
                        '__add__', '__radd__','__setitem__' ])
persistent.list.PersistentList.__Security_checker__ = list_checker

#defineChecker(persistent.dict.PersistentDict,)
#defineChecker(persistent.list.PersistentList,)

# zope transcation stuff
ModuleSecurityInfo("transaction").declarePublic("savepoint")
ModuleSecurityInfo('zope.interface').declarePublic('alsoProvides')
