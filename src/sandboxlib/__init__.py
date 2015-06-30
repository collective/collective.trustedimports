# -*- coding: utf-8 -*-
"""Init and utils."""
from AccessControl import allow_class, ModuleSecurityInfo
from Products.PythonScripts.Utility import allow_module

# Whitelist pdf functions
allow_module('pretaweb.plomino2pdf.api')
pdf_api = ModuleSecurityInfo('pretaweb.plomino2pdf.api')
pdf_api.declarePublic('generate_pdf')

# Whitelist email functions
allow_module('email.mime.multipart')
multipart = ModuleSecurityInfo('email.mime.multipart')
multipart.declarePublic('MIMEMultipart')
allow_module('email.mime.text')
text = ModuleSecurityInfo('email.mime.text')
text.declarePublic('MIMEMultipart')
allow_module('email.mime.application')
application = ModuleSecurityInfo('email.mime.application')
application.declarePublic('MIMEApplication')

# Whitelist plone.api
allow_module('plone.api.portal')
portal = ModuleSecurityInfo('plone.api.portal')
portal.declarePublic('get_tool')
