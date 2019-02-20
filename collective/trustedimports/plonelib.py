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

defineChecker(persistent.dict.PersistentDict,             )
defineChecker(persistent.list.PersistentList,


#TODO: move into taskqueue
ModuleSecurityInfo("collective.taskqueue.taskqueue").declarePublic("add")

# RichTextValue
try:
    import plone.app.textfield.value
except ImportError:
    plone.app.textfield.value = None

if plone.app.textfield.value is not None:
    plone.app.textfield.value.RichTextValue._security = sec_RichTextValue = ClassSecurityInfo()
    sec_RichTextValue.declareObjectPublic()
    sec_RichTextValue.declarePrivate('raw')
    sec_RichTextValue.declarePrivate('encoding')
    sec_RichTextValue.declarePrivate('raw_encoded')
    sec_RichTextValue.declarePrivate('mimeType')
    sec_RichTextValue.declarePrivate('outputMimeType')
    sec_RichTextValue.declarePrivate('output_relative_to')
    sec_RichTextValue.setDefaultAccess(1)
    sec_RichTextValue.apply(plone.app.textfield.value.RichTextValue)
    InitializeClass(plone.app.textfield.value.RichTextValue)

# datastream
try:
    import Products.PortalTransforms.data
except ImportError:
    Products.PortalTransforms.data = None

if Products.PortalTransforms.data is not None:
    Products.PortalTransforms.data.datastream._security = sec_datastream = ClassSecurityInfo()
    sec_datastream.declareObjectPublic()
    sec_datastream.declarePrivate('setData')
    sec_datastream.declarePrivate('setSubObjects')
    sec_datastream.declarePrivate('getSubObjects')
    sec_datastream.declarePrivate('setCacheable')
    sec_datastream.setDefaultAccess(1)
    sec_datastream.apply(Products.PortalTransforms.data.datastream)
    InitializeClass(Products.PortalTransforms.data.datastream)

# NamedBlobFile
try:
    import plone.namedfile.file
except ImportError:
    plone.namedfile.file = None

if plone.namedfile.file is not None:
    plone.namedfile.file.NamedBlobFile._security = sec_NamedBlobFile = ClassSecurityInfo()
    sec_NamedBlobFile.declareObjectPublic()
    sec_NamedBlobFile.declarePrivate('open')
    sec_NamedBlobFile.declarePrivate('openDetached')
    sec_NamedBlobFile.declarePrivate('_setData')
    sec_NamedBlobFile.setDefaultAccess(1)
    sec_NamedBlobFile.apply(plone.namedfile.file.NamedBlobFile)
    InitializeClass(plone.namedfile.file.NamedBlobFile)
