Python stdlib
=============

Regular Expressions (re)
------------------------

>>> print teval("import re; return re.findall('Isaac', 'Isaac Asimov')")
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

Os (not supported)
------------------

>>> print teval("import os; return os.environ")
Traceback (most recent call last):
...
Unauthorized: import of 'os' is unauthorized