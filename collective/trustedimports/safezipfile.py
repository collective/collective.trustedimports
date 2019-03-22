import zipfile
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from zipfile import ZipFile as _ZipFile, ZIP_STORED, ZipInfo
from collective.trustedimports.util import monkey_patch_if_restricted

# monkey patching zipfile

monkey_patch_if_restricted(_ZipFile.__init__, lambda file: not isinstance(file, basestring))
monkey_patch_if_restricted(_ZipFile.extract)
monkey_patch_if_restricted(_ZipFile.extractall)
monkey_patch_if_restricted(_ZipFile.write)

#zipfile.ZipFile = SafeZipFile

ModuleSecurityInfo('zipfile').declarePublic('ZipFile')

allow_class(_ZipFile)
ModuleSecurityInfo('zipfile').declarePublic('ZIP64_LIMIT',
                                             'ZIP_FILECOUNT_LIMIT',
                                             'ZIP_MAX_COMMENT',
                                             'ZIP_STORED',
                                             'ZIP_DEFLATED',
                                             'ZipInfo')
allow_class(ZipInfo)
