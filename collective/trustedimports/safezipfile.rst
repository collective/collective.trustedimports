Zip
===

When used in RestrictedPython we can still use ZipFile

>>> teval("from zipfile import ZipFile; from StringIO import StringIO; return ZipFile(StringIO(),'w')")
<collective.trustedimports.safezipfile.SafeZipFile ... at ...>


but we can't use it to open files on the disk

>>> teval("import zipfile; zipfile.ZipFile('myfile.zip')")
Traceback (most recent call last):
...
Unauthorized: Not supported by SafeZipFile in this context

or use it to extract files to disk
>>> teval("from zipfile import ZipFile; from StringIO import StringIO; ZipFile(StringIO(),'w').extractall()")
Traceback (most recent call last):
...
Unauthorized: Not supported by SafeZipFile in this context

We can still use it when not in a PythonScript
>>> import zipfile; zipfile.ZipFile('myfile.zip')
Traceback (most recent call last):
...
IOError: [Errno 2] No such file or directory: 'myfile.zip'


