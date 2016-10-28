from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module


#Uses files but doesn't open them. need to double check
allow_module('csv')
# ModuleSecurityInfo('nntplib').declarePublic('NNTP',
#   'error_reply', 'error_temp', 'error_perm', 'error_proto')
import csv
allow_class(csv.DictReader)
allow_class(csv.DictWriter)
allow_class(csv.Dialect)
allow_class(csv.excel)
allow_class(csv.excel_tab)
allow_class(csv.Sniffer)
