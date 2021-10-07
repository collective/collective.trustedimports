from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from collective.trustedimports.util import wrap_protected, whitelist_module


import docxtpl

file_like = lambda f: hasattr(f, 'read')

wrap_protected(docxtpl.DocxTemplate.__init__, lambda docx: file_like(docx))
wrap_protected(docxtpl.DocxTemplate.save, lambda filename: file_like(filename))
wrap_protected(docxtpl.DocxTemplate.write_xml, lambda filename: file_like(filename))
#ModuleSecurityInfo('docxtpl').declarePublic('DocxTemplate')
#allow_class(docxtpl.DocxTemplate)
whitelist_module('docxtpl', ['DocxTemplate'], ['DocxTemplate'])


# import docx
# wrap_protected(docx.document.Document.__init__, lambda element: file_like(element))
# wrap_protected(docx.document.Document, lambda path_or_stream: file_like(path_or_stream))

#TODO: docx has a lot of methods to whitelist. 

#TODO: need to look if there is a way to embed content that might allow reading filesystem files



# allow_class(_ZipFile)
# ModuleSecurityInfo('zipfile').declarePublic('ZIP64_LIMIT',
#                                              'ZIP_FILECOUNT_LIMIT',
#                                              'ZIP_MAX_COMMENT',
#                                              'ZIP_STORED',
#                                              'ZIP_DEFLATED',
#                                              'ZipInfo')
# allow_class(ZipInfo)
