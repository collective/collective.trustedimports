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

We can make a get request using the requests library
>>> import requests
>>> response = requests.get("https://example.com")
>>> response
<Response [200]>
>>> "Example Domain" in response.content
True

We can also make a post request
>>> import requests
>>> response = requests.post("https://postman-echo.com/post", data={"post_data": "This is expected to be sent back as part of response body."})
>>> response
<Response [200]>
>>> response.json()["json"]["post_data"]
u'This is expected to be sent back as part of response body.'


#TODO Add tests for allowlist and blocklist behaviour using requests