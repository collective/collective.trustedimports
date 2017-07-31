from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zope.security.checker import defineChecker, CheckerPublic, NamesChecker


allow_module("plone.subrequest")

# Whitelist plone.api
allow_module('plone.api.portal')
portal = ModuleSecurityInfo('plone.api.portal')
portal.declarePublic('get_tool')

# zope transcation stuff
ModuleSecurityInfo("transaction").declarePublic("savepoint")

# Basic ZODB stuff
import persistent.list
import persistent.dict
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

#defineChecker(persistent.dict.PersistentDict,             )
#defineChecker(persistent.list.PersistentList,


#TODO: move into taskqueue
ModuleSecurityInfo("collective.taskqueue.taskqueue").declarePublic("add")
