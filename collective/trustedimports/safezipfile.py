import zipfile
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from zipfile import ZipFile as _ZipFile, ZIP_STORED, ZipInfo
from collective.trustedimports.util import wrap_protected, whitelist_module

# monkey patching zipfile

wrap_protected(_ZipFile.__init__, lambda file: not isinstance(file, basestring))
wrap_protected(_ZipFile.extract)
wrap_protected(_ZipFile.extractall)
wrap_protected(_ZipFile.write)


# ModuleSecurityInfo('zipfile').declarePublic('ZipFile')
#
# allow_class(_ZipFile)
# ModuleSecurityInfo('zipfile').declarePublic('ZIP64_LIMIT',
#                                              'ZIP_FILECOUNT_LIMIT',
#                                              'ZIP_MAX_COMMENT',
#                                              'ZIP_STORED',
#                                              'ZIP_DEFLATED',
#                                              'ZipInfo')
#allow_class(ZipInfo)

whitelist_module('zipfile',
                 ['ZipInfo','ZipFile'],
                 [
                     'ZIP64_LIMIT',
                     'ZIP_FILECOUNT_LIMIT',
                     'ZIP_MAX_COMMENT',
                     'ZIP_STORED',
                     'ZIP_DEFLATED',
                     'ZipInfo']
                 )