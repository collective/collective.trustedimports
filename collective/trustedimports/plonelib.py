from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zope.security.checker import defineChecker, CheckerPublic, NamesChecker

allow_module("plone.subrequest")

# Whitelist plone.api
allow_module('plone.api.portal')
portal = ModuleSecurityInfo('plone.api.portal')
portal.declarePublic('get_tool')


# Whitelist plone.protect
ModuleSecurityInfo('plone.protect.utils').declarePublic('safeWrite')
ModuleSecurityInfo('plone.protect.interfaces').declarePublic('IDisableCSRFProtection')
ModuleSecurityInfo('plone.protect.utils').declarePublic('addTokenToUrl')


# RichTextValue
import plone.app.textfield.value

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
import Products.PortalTransforms.data

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
import plone.namedfile.file

plone.namedfile.file.NamedBlobFile._security = sec_NamedBlobFile = ClassSecurityInfo()
sec_NamedBlobFile.declareObjectPublic()
sec_NamedBlobFile.declarePrivate('open')
sec_NamedBlobFile.declarePrivate('openDetached')
sec_NamedBlobFile.declarePrivate('_setData')
sec_NamedBlobFile.setDefaultAccess(1)
sec_NamedBlobFile.apply(plone.namedfile.file.NamedBlobFile)
InitializeClass(plone.namedfile.file.NamedBlobFile)

# Whitelist internationalisation and normalisation
from plone.i18n.normalizer.adapters import UserPreferredURLNormalizer
from plone.i18n.normalizer import idnormalizer
ModuleSecurityInfo('plone.i18n.normalizer.interfaces').declarePublic('IUserPreferredURLNormalizer')
allow_class(UserPreferredURLNormalizer)
allow_class(idnormalizer)