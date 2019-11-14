SOAP (Zeep)
===========

When used in RestrictedPython we can still use Zeep

>>> teval("from zeep import Client; return Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL').service.CapitalCity('NL')")
'Amsterdam'


We can't set transport option for WSDL service

>>> teval("from zeep import Client;client = Client('blah', transport = 'something')")
Traceback (most recent call last):
...
ValueError: Argument(s) 'transport' have values not supported in a restricted python call

or set transport directly

>>> teval("from zeep import Client; Client('blah').transport ='something'")
Traceback (most recent call last):
...
ValueError: unguard attribute set/del at Script (Python):1


We can use bind

>>> teval("from zeep import Client;return Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL').bind('CountryInfoService', 'CountryInfoServiceSoap').CapitalCity('NL')")
'Amsterdam'


URL Restrictions
----------------

*WARNING: The urls referenced in a downloaded WSDL are not currently checked for safety.*

If we define a url blacklist environment variable, we can allow all urls to be access except for those on the blacklist

>>> import os
>>> os.environ["SAFEIMPORTS_URL_BLACKLIST"] = "www.w3schools.com;/*.asmx"


We can't open connection to URL in blacklist

>>> teval("from zeep import Client;return Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: URL https://www.w3schools.com/Xml/tempconvert.asmx?WSDL is not allowed to be accessed. URL is in the blacklist

We cann't open connection to URL wildcard in blacklist

>>> teval("from zeep import Client;return Client('http://www.dneonline.com/calculator.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: URL http://www.dneonline.com/calculator.asmx?WSDL is not allowed to be accessed. URL is in the blacklist

However, we can open a connection to a URL not in the blacklist

>>> teval("from zeep import Client;return Client('https://raw.githubusercontent.com/mvantellingen/python-zeep/master/tests/wsdl_files/soap.wsdl')")
<zeep.client.Client ...>

'create_service' has restricted urls

>>> teval("from zeep import Client;client = Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL');return client.create_service('{https://www.w3schools.com/xml/}TempConvertSoap', 'http://www.w3schools.com')")
Traceback (most recent call last):
...
ValueError: URL https://www.w3schools.com/Xml/tempconvert.asmx?WSDL is not allowed to be accessed. URL is in the blacklist


>>> del os.environ["SAFEIMPORTS_URL_BLACKLIST"]


If we define a url allowlist environment variable, we can block all urls except for those in the allowlist

>>> import os

We should be able to open a url defined in the allowlist
>>> os.environ["SAFEIMPORTS_URL_ALLOWLIST"] = "https://www.w3schools.com/Xml/tempconvert.asmx?WSDL"
>>> teval("from zeep import Client;return Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL')")
<zeep.client.Client ...>

But we should not have access to a URL not included on the allowlist
>>> teval("from zeep import Client;return Client('https://raw.githubusercontent.com/mvantellingen/python-zeep/master/tests/wsdl_files/soap.wsdl')")
Traceback (most recent call last):
...
ValueError: URL https://raw.githubusercontent.com/mvantellingen/python-zeep/master/tests/wsdl_files/soap.wsdl is not allowed to be accessed. URL is outside of allowlist

>>> del os.environ["SAFEIMPORTS_URL_ALLOWLIST"]


We should also be able to specify a wildcard to allow multile URLs from the same domain
>>> os.environ["SAFEIMPORTS_URL_ALLOWLIST"] = "https://raw.githubusercontent.com/mvantellingen/python-zeep/master/tests/wsdl_files/soap*"
>>> teval("from zeep import Client;return Client('https://raw.githubusercontent.com/mvantellingen/python-zeep/master/tests/wsdl_files/soap.wsdl')")
<zeep.client.Client ...>
>>> teval("from zeep import Client;return Client('https://raw.githubusercontent.com/mvantellingen/python-zeep/master/tests/wsdl_files/soap_header.wsdl')")
<zeep.client.Client ...>

But we should not be able to access URLs from that domain which aren't included in the wildcard
>>> teval("from zeep import Client;return Client('https://raw.githubusercontent.com/mvantellingen/python-zeep/master/tests/wsdl_files/http.wsdl')")
Traceback (most recent call last):
...
ValueError: URL https://raw.githubusercontent.com/mvantellingen/python-zeep/master/tests/wsdl_files/http.wsdl is not allowed to be accessed. URL is outside of allowlist

And we still shouldn't be able to access URLs outside of that domain
>>> teval("from zeep import Client;return Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: URL https://www.w3schools.com/Xml/tempconvert.asmx?WSDL is not allowed to be accessed. URL is outside of allowlist

>>> del os.environ["SAFEIMPORTS_URL_ALLOWLIST"]


We can import exceptions too

>>> teval("from zeep.exceptions import Error")
