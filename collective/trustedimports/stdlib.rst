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


>>> teval("return '-'.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(3))")
'...-...-...'


UUID
----

>>> teval("import uuid; return uuid.uuid4()")
UUID('...-...-...-...-...')

>>> teval("import uuid; return str(uuid.uuid1().get_hex().upper()[0:6])")
'...'

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


Time
----
#>>> print teval('from time import strptime; return strptime("30 Nov 00", "%d %b %y")')
#time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
#                 tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)


Os (not supported)
------------------

>>> print teval("import os; return os.environ")
Traceback (most recent call last):
...
Unauthorized: import of 'os' is unauthorized

