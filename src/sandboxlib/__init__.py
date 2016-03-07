# -*- coding: utf-8 -*-
"""Init and utils."""
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
import csv
import email
import zip
import python
import plone




#TODO: Doesn't belong in this package
# Whitelist pdf functions
allow_module('pretaweb.plomino2pdf.api')
pdf_api = ModuleSecurityInfo('pretaweb.plomino2pdf.api')
pdf_api.declarePublic('generate_pdf')


