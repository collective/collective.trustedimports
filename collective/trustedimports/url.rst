urllib
===========

We want to allow parsing and quoting

>>> teval("import urllib;return urllib.quote('châteu', safe='')")
'ch%C3%A2teu'


We also can parse with urlparse

>>> print teval("from urlparse import urlparse;return urlparse('https://www.google.com/')")
ParseResult...

At this point we don't want to allow access the internet

We cannot user other function of urllib, such as

>>> teval("import urllib;urllib.urlopen('https://www.google.com')")
Traceback (most recent call last):
...
Unauthorized: You are not allowed to access 'urlopen' in this context


We can also use urljoin

>>> teval("from urlparse import urljoin; return urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')")
'http://www.cwi.nl/%7Eguido/FAQ.html'


We can use these functions in system python

>>> import urllib
>>> urllib.urlopen('https://www.google.com')
<addinfourl at ...

>>> from urlparse import urljoin
>>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')
'http://www.cwi.nl/%7Eguido/FAQ.html'


