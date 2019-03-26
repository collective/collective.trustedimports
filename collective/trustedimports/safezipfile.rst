ZIPFILE
=======

When used in RestrictedPython we can still use ZipFile

>>> teval("from zipfile import ZipFile; from StringIO import StringIO; return ZipFile(StringIO(),'w')")
<zipfile.ZipFile ... at ...>


but we can't use it to open files on the disk

>>> teval("import zipfile; zipfile.ZipFile('myfile.zip')")
Traceback (most recent call last):
...
ValueError: Argument(s) 'file' have values not supported in a restricted python call

or use it to extract files to disk

>>> teval("from zipfile import ZipFile; from StringIO import StringIO; ZipFile(StringIO(),'w').extractall()")
Traceback (most recent call last):
...
ValueError: Method 'extractall' not supported in a restricted python call

>>> teval("from zipfile import ZipFile; from StringIO import StringIO; ZipFile(StringIO(),'w').extract()")
Traceback (most recent call last):
...
ValueError: Method 'extract' not supported in a restricted python call

We can still use it when not in a PythonScript

>>> import zipfile; zipfile.ZipFile('myfile.zip')
Traceback (most recent call last):
...
IOError: [Errno 2] No such file or directory: 'myfile.zip'


