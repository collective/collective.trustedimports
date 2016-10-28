Zip
===

We can import the zip module as normal

>>> teval("import zip")

however we can't use the normal constructor

>>> teval("import zip; zip.Zipfile('myfile.zip')")
>>> excepton

Instead we have to use a special class method

>>> teval("import zip; zip.Zipfile.SafeZipfile()")


