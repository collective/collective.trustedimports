Changelog
=========

0.2 (unreleased)
----------------
- Added Plone URL normalisers to allowed imports [jeffersonbledsoe]
- Fixed test suite [jeffersonbledsoe]
- Added `plone.protect.utils.addTokenToUrl` to allowed imports [jeffersonbledsoe]
- Added plone protection to allowed imports for disabling CSRF checking [djay]
- Added `urllib` and `urlparse` to allowed imports [nngu6036]
- Fixed `zeep.bind` and `zeep.create_service` now being allowed [nngu6036]
- Added `zeep` to allowed imports for SOAP support [nngu6036]
- Fixed name checker to check for classes [djay]
- Changed tests to run all `.rst` files as part of the test suite [djay]
- Changed raw monkey patch wrapping to use `is_url_allowed` function [djay]
- Added `email.encoders.encode_base64` and `email.encoders` to allowed imports [instification]
- switched to using `z3c.autoinclude` to ensure security gets loaded after others [djay]
- add utils helper to monkey patch methods that should only be used outside of restricted python [djay]


0.1 (unreleased)
----------------
- Added `phonenumbers` to allowed imports [nngu6036]
- Added `NamedBlobFile.Data`, `datastream.getData` and `RichTextValue.output` to allowed imports [ivanteoh]
- Fixed security checker being created twice [djay]
- Added `base64.b64encode` and `base64.b64decode` to allowed imports [instification]
- Added `time` and `email.Utils` to allowed imports [ivanteoh]
- Added `lxml_xpath` to allowed imports [ivanteoh]
- Added `defusedxml.ElementTree` and `xml.etree.ElementTree` to allowed imports [ivanteoh]
- Added `email.utils`, `email.errors`, `email.charset`, `email.header`, `email.generator` and `email.parser` to allowed imports [djay]
- Added various functions from `email.encoders` and `email.mime` to allowed imports [djay]
- Added `pystache.render` to allowed imports [displacedaussie]
- Fixed monkey patching security issue in ZipFile api [djay]
- Added `random.SystemRandom` and `uuid` to allowed imports [djay]
- Added various function from `email.mime` to allowed imports [djay]
- Added `plone.subrequest`, `plone.api.portal`, `plone.api.portal.get_tool` and `transaction` to allowed imports [djay]
- Added `re`, `random`, and `itertools` to allowed imports [djay]
- Added `SafeZip` to allowed imports by wrapping `ZipFile`
- Added `M2Crypto` to allowed imports [djay]
