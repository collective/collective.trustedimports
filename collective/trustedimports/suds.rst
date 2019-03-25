Zip
===

When used in RestrictedPython we can still use Suds

>>> teval("from suds.client import Client; from suds import WebFault,MethodNotFound;return Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')")
...True


We cann't set transport option for WSDL service

>>> teval("from suds.client import Client;from suds.transport.https import HttpAuthenticated;client = Client('https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl',transport=HttpAuthenticated())")
...True

>>> teval("from suds.client import Client;from suds.transport.https import HttpAuthenticated;client = Client('https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl');client.set_options(transport=HttpAuthenticated())")
...True

We can get execute method from WSDL service

>>> teval("from suds.client import Client; client = Client('https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl');result=client.service.ConvertSpeed(100, 'kilometersPerhour', 'milesPerhour');assert result == 62.137")
...True


We can still use it when not in a PythonScript

>>> from suds.client import Client; from suds import WebFault,MethodNotFound;
>>> client = Client('https://graphical.weather.gov/xml/SOAP_server/ndfdXMLserver.php?wsdl')
>>> result=client.service.ConvertSpeed(100, 'kilometersPerhour', 'milesPerhour')
>>> result == 62.137
...True
