SOAP
===

When used in RestrictedPython we can still use Suds

>>> teval("from zeep import Client;return Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')")
<zeep.client.Client ... at ...>

We cann't set transport option for WSDL service

>>> teval("from zeep import Client;client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL', settings = {'force_https':True})")
Traceback (most recent call last):
...
ValueError: Argument(s) 'wsdl,settings' have values not supported in a restricted python call

>>> teval("from zeep import Client;client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL', settings = {'extra_http_headers':''})")
Traceback (most recent call last):
...
ValueError: Argument(s) 'wsdl,settings' have values not supported in a restricted python call

We cann't open connection to URL in blacklist
>>> teval("from zeep import Client;return Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: Argument(s) 'wsdl' have values not supported in a restricted python call

We cann't open connection to URL wildcard in blacklist
>>> teval("from zeep import Client;return Client('http://www.dneonline.com/calculator.asmx?WSDL')")
Traceback (most recent call last):
...
ValueError: Argument(s) 'wsdl' have values not supported in a restricted python call

We cann't call method 'bind'
>>> teval("from zeep import Client;return Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL');client.bind()")
Traceback (most recent call last):
...
ValueError: Argument(s) 'wsdl' have values not supported in a restricted python call

We cann't call method 'create_service'
>>> teval("from zeep import Client;return Client('https://www.w3schools.com/Xml/tempconvert.asmx?WSDL');client.create_service()")
Traceback (most recent call last):
...
ValueError: Argument(s) 'wsdl' have values not supported in a restricted python call

We can call WSDL method as usual
>>> teval("from zeep import Client; client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL');result=client.service.CapitalCity('NL');assert result == 'Amsterdam'")


We can still use it when not in a PythonScript

>>> from zeep import Client
>>> client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')
>>> result = client.service.CapitalCity('NL')
>>> result
'Amsterdam'
