Zip
===

When used in RestrictedPython we can still use Suds

>>> teval("from suds.client import Client; from suds import WebFault,MethodNotFound;return Client('')")
Traceback (most recent call last):
...
ValueError: unknown url type:

>>> from suds.client import Client; from suds import WebFault,MethodNotFound;
>>> Client('')
Traceback (most recent call last):
...
ValueError: unknown url type:

