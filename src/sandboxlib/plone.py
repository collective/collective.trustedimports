from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module


allow_module("plone.subrequest")

# Whitelist plone.api
allow_module('plone.api.portal')
portal = ModuleSecurityInfo('plone.api.portal')
portal.declarePublic('get_tool')

# zope transcation stuff
ModuleSecurityInfo("transaction").declarePublic("savepoint")


#TODO: move into taskqueue
ModuleSecurityInfo("collective.taskqueue.taskqueue").declarePublic("add")
