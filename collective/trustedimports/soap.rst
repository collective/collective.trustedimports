SOAP
===

When used in RestrictedPython we can still use Zeep

>>> teval("from zeep import Client;return Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')")
<zeep.client.Client ... at ...>


We can call WSDL method as usual
>>> teval("from zeep import Client; return Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL').service.CapitalCity('NL')")
'Amsterdam'



>>> teval("from zeep.exceptions import Error;raise Error('Test error')")
Traceback (most recent call last):
...
Error: Test error


We can't set transport option for WSDL service

>>> teval("from zeep import Client;client = Client('blah', transport = 'something')")
Traceback (most recent call last):
...
ValueError: Argument(s) 'transport' have values not supported in a restricted python call

>>> import os
>>> os.environ["SAFEIMPORTS_URL_BLACKLIST"] = "https://www.w3schools.com/Xml/tempconvert.asmx?WSDL;http://www.dneonline.com/*.asmx?WSDL"


We cann't open connection to URL in blacklist
>>> teval("from zeep import Client;return Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: URL https://www.w3schools.com/Xml/tempconvert.asmx?WSDL is not allowed to be accessed

We cann't open connection to URL wildcard in blacklist
>>> teval("from zeep import Client;return Client('http://www.dneonline.com/calculator.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: URL http://www.dneonline.com/calculator.asmx?WSDL is not allowed to be accessed

>>> del os.environ["SAFEIMPORTS_URL_BLACKLIST"]

We cann't call method 'bind'
>>> teval("from zeep import Client;client = Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL');client.bind()")
Traceback (most recent call last):
...
ValueError: Method 'bind' not supported in a restricted python call


We can still use it when not in a PythonScript

>>> from zeep import Client
>>> client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')
>>> service = client.bind('CountryInfoService', 'CountryInfoServiceSoap')
>>> result = service.CapitalCity('NL')
>>> result
'Amsterdam'


We cann't call method 'create_service'
>>> teval("from zeep import Client;client = Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL');client.create_service()")
Traceback (most recent call last):
...
ValueError: Method 'create_service' not supported in a restricted python call
