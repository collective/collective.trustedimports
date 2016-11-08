Zip
===

We can't use the normal constructor

>>> teval("import zipfile; zipfile.ZipFile('myfile.zip')")
Traceback (most recent call last):
...
Unauthorized: You are not allowed to access 'ZipFile' in this context

Instead we have to use a special class method

>>> teval("from collective.trustedimports.safezipfile import SafeZipFile; SafeZipFile('/etc/password')")
Traceback (most recent call last):
...
NotImplementedError: Paths not supported by SafeZipFile

>>> teval("from collective.trustedimports.safezipfile import SafeZipFile; from StringIO import StringIO; return SafeZipFile(StringIO(),'w')")
<collective.trustedimports.safezipfile.SafeZipFile instance at ...>

