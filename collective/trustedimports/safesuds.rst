Zip
===

When used in RestrictedPython we can still use Suds

>>> teval("from suds.client import Client; from suds import WebFault,MethodNotFound;return Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')")
<suds.client.Client ... at ...>

We cann't set transport option for WSDL service

>>> teval("from suds.client import Client;from suds.transport.https import HttpAuthenticated;client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL', transport = HttpAuthenticated())")
Traceback (most recent call last):
...
ValueError: Argument(s) 'url,transport' have values not supported in a restricted python call

>>> teval("from suds.client import Client;from suds.transport.https import HttpAuthenticated;client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL');client.set_options(transport = HttpAuthenticated())")
Traceback (most recent call last):
...
ValueError: Argument(s) 'transport' have values not supported in a restricted python call

We cann't open connection to URL in blacklist
>>> teval("from suds.client import Client; from suds import WebFault,MethodNotFound;return Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: Argument(s) 'url' have values not supported in a restricted python call

We can call WSDL method as usual
>>> teval("from suds.client import Client; client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL');result=client.service.CapitalCity('NL');assert result == 'Amsterdam'")


We can still use it when not in a PythonScript

>>> from suds.client import Client
>>> from suds import WebFault,MethodNotFound
>>> client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')
>>> result = client.service.CapitalCity('NL')
>>> result
Amsterdam
