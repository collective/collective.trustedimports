Zip
===

We can import the zip module as normal

>>> teval("import zipfile")

however we can't use the normal constructor

>>> teval("zipfile.Zipfile('myfile.zip')")
Unauthorized: import of 'zip' is unauthorized

Instead we have to use a special class method

>>> teval("from collective.trustedimports.safezipfile import SafeZipFile; SafeZipfile()")


