Python stdlib
=============

Regular Expressions (re)
------------------------

>>> print teval("import re; return re.findall('Isaac', 'Isaac Asimov')")
['Isaac']

>>> print teval("import re; return re.compile('Isaac').findall('Isaac Asimov')")
['Isaac']

Random
------

>>> print teval("import random; return random.random()")
0...


Itertools
---------

>>> for i in teval("from itertools import izip; return izip([1, 2, 3], ['a', 'b', 'c'])"):
...    print i
(1, 'a')
(2, 'b')
(3, 'c')

StringIO
--------

>>> print teval("import StringIO; return StringIO.StringIO('blah').read()")
blah

We can also create cStringIO to pass to other libraries
>>> print teval("import cStringIO; return cStringIO.StringIO('foo')")
<cStringIO.StringI object at ...>

but we can't access cStringIO objects in restricted python
>>> print teval("import cStringIO; return cStringIO.StringIO('bah').read()")
Traceback (most recent call last):
...
Unauthorized: You are not allowed to access 'read' in this context


CSV
-------

>>> print teval("""import csv; import StringIO; return list(csv.reader(StringIO.StringIO('"A","B","C"\\n1,2,3')))""")
[['A', 'B', 'C'], ['1', '2', '3']]

Os (not supported)
------------------

>>> print teval("import os; return os.environ")
Traceback (most recent call last):
...
Unauthorized: import of 'os' is unauthorized