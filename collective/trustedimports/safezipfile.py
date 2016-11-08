from inspect import stack
import zipfile
from AccessControl import allow_class, ModuleSecurityInfo, ClassSecurityInfo, Unauthorized
from AccessControl.class_init import InitializeClass
from Products.PythonScripts.Utility import allow_module
from zipfile import ZipFile as _ZipFile, ZIP_STORED, ZipInfo
#from exceptions import NotImplementedError

def restricted_python_call():
    # HACK: must be a better way to do this
    caller = stack()[2][1]
    return caller == 'Script (Python)'

class SafeZipFile(_ZipFile):
    """ SafeZipFile
    """

    def __init__(self, file, mode="r", compression=ZIP_STORED, allowZip64=False):


        if isinstance(file, basestring) and restricted_python_call():
            raise Unauthorized("Not supported by SafeZipFile in this context")

        return _ZipFile.__init__(self, file, mode, compression, allowZip64)



    def extract(self, member, path=None, pwd=None):
        """Extract a member from the archive to the current working directory,
           using its full name. Its file information is extracted as accurately
           as possible. `member' may be a filename or a ZipInfo object. You can
           specify a different directory using `path'.
        """
        if restricted_python_call():
            raise Unauthorized("Not supported by SafeZipFile in this context")
        else:
            return _ZipFile.extract(member, path, pwd)

    def extractall(self, path=None, members=None, pwd=None):
        """Extract all members from the archive to the current working
           directory. `path' specifies a different directory to extract to.
           `members' is optional and must be a subset of the list returned
           by namelist().
        """
        if restricted_python_call():
            raise Unauthorized("Not supported by SafeZipFile in this context")
        else:
            return _ZipFile.extractall(path, members, pwd)

    def write(self, filename, arcname=None, compress_type=None):
        """Put the bytes from filename into the archive under the name
        arcname."""
        if restricted_python_call():
            raise Unauthorized("Not supported by SafeZipFile in this context")
        else:
            return _ZipFile.write(filename, arcname, compress_type)

# monkey patching zipfile
zipfile.ZipFile = SafeZipFile

ModuleSecurityInfo('collective.trustedimports.safezipfile').declarePublic('SafeZipFile')

allow_class(SafeZipFile)
ModuleSecurityInfo('zipfile').declarePublic('ZIP64_LIMIT',
                                             'ZIP_FILECOUNT_LIMIT',
                                             'ZIP_MAX_COMMENT',
                                             'ZIP_STORED',
                                             'ZIP_DEFLATED',
                                             'ZipInfo')
allow_class(ZipInfo)
