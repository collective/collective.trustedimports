Docxtpl
=======

When used in RestrictedPython we can still use Docxtmp

>>> teval("from docxtpl import DocxTemplate; from StringIO import StringIO; return DocxTemplate(StringIO())")
Traceback (most recent call last):
...
BadZipfile: File is not a zip file

but we can't use it to open files on the disk

>>> teval("import docxtpl; docxtpl.DocxTemplate('my.docx')")
Traceback (most recent call last):
...
ValueError: Argument(s) 'docx' have values not supported in a restricted python call


We can still use it when not in a PythonScript

>>> import docxtpl; docxtpl.DocxTemplate('myfile.docx')
Traceback (most recent call last):
...
PackageNotFoundError: Package not found at 'myfile.docx'


We don't allow access to internal methods

#>>> teval("from docxtpl import DocxTemplate; from StringIO import StringIO; DocxTemplate(StringIO()).extractall()")
#Traceback (most recent call last):
#...
#ValueError: Method 'extractall' not supported in a restricted python call

#>>> teval("from docxtpl import DocxTemplate; from StringIO import StringIO; DocxTemplate(StringIO()).extract()")
#Traceback (most recent call last):
#...
#ValueError: Method 'extract' not supported in a restricted python call



