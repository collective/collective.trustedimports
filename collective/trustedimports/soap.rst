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

or set transport directly
>>> teval("from zeep import Client; Client('blah').transport ='something'")
Traceback (most recent call last):
...
ValueError: unguard attribute set/del at Script (Python):1

>>> import os
>>> os.environ["SAFEIMPORTS_URL_BLACKLIST"] = "www.w3schools.com;/*.asmx"



We can use bind
>>> teval("from zeep import Client;return Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL').bind('CountryInfoService', 'CountryInfoServiceSoap').CapitalCity('NL')")
'Amsterdam'



We can't open connection to URL in blacklist
>>> teval("from zeep import Client;return Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: URL https://www.w3schools.com/Xml/tempconvert.asmx?WSDL is not allowed to be accessed

We cann't open connection to URL wildcard in blacklist
>>> teval("from zeep import Client;return Client('http://www.dneonline.com/calculator.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: URL http://www.dneonline.com/calculator.asmx?WSDL is not allowed to be accessed

'create_service' has restricted urls
>>> teval("from zeep import Client;client = Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL');return client.create_service('{https://www.w3schools.com/xml/}TempConvertSoap', 'http://www.w3schools.com')")
Traceback (most recent call last):
...
ValueError: URL https://www.w3schools.com/Xml/tempconvert.asmx?WSDL is not allowed to be accessed


>>> del os.environ["SAFEIMPORTS_URL_BLACKLIST"]
