collective.trustedimports
=========================

Introduction
------------

This package whitelists a number of common Python packages for use in
restrictedPython allowing you to import them and use them like in normal python.

Some libraries include apis which are insecure such as providing filesystem or
internet access.
In these cases an alternative import is provided which wraps the library in
a secure way.

It is designed to be a single download to give your zope/plone instance access
to a lot more power TTW from tools such as
Plomino, PloneFormGen, collective.listingviews and other addons that allow
power plone development.

Usage
-----

This module is loaded using z3c.autoinclude so in plone this will be handled 
automatically. In other python code you may need to manually import the particular
module to initialise that additional security declarations e.g.

```python
import collective.trustedimports.pystache

```

Contents
--------

Currently support libraries which can use used without modification are:

- [stdlib supported](collective/trustedimports/stdlib.rst)
- [zipfile supported](collective/trustedimports/safezipfile.rst)
- [email/mimetype/M2Crypto](collective/trustedimports/trustedemail.rst)
- [SOAP zeep Client](collective/trustedimports/soap.rst)
- [pystache](collective/trustedimports/pystache.rst)
- [phonenumbers](collective/trustedimports/phonenumbers.rst)
- [LXML](collective/trustedimports/lxml.rst)
- [defusedxml](collective/trustedimports/defusedxml.rst)
- [zope apis](collective/trustedimports/_zope.rst)
- [plone apis](collective/trustedimports/plonelib.rst)
- [collective.taskqueue](collective/trustedimports/collective_taskqueue.rst)

Contribute
----------
If you think another library should be be made importable contribute on
[github](https://github.com/collective/collective.trustedimports)

How to whitelist a module
-------------------------

1. First thing to do is decide if you can contribute to the code itself, then perhaps the best place is to submit a patch to your thirdparty code to allow it to be imported in restricted python.

2. Next determine if the module is safe. Things you should look for are if any function in the module:
   - involve writing or reading from files?
   - reveal sensitive system information?
   - have the capacity to block or take a long time?
   - make network calls?
   - allow setting arbitrary attributes of passed in objects?
   
3. Find a place in trusedimports for your whitelist. e.g. [stdlib.py](collective/trustedimports/stdlib.py)
   or add an additional file. Ensure this file is included in ```configure.zcml```. If you are whitelisting
   a pypi package it should go into its own file and conditions in ```configure.zcml``` so
   there are no errors when that package is not available.

4. Add your whitelist
   - e.g. ```whitelist_module(module='base64', classes=['b64encode', 'b64decode'])```
   - Only whitelist functions that are safe. For example never whitelist functions that access
     local file system files.
   - you can use utils.wrap_protected to monkey patch methods that should be restricted
   - you can use our [convenience function](https://github.com/collective/collective.trustedimports/blob/master/collective/trustedimports/util.py#L9) to handle whitelisting in both zope.security and Products.PythonScripts at the same time (there are two different systems of restricted python).
   - If what you want to whitelist does include unsafe calls such as access to the filesystem, there are [ways to monkey patch to make it safe](https://github.com/collective/collective.trustedimports/blob/master/collective/trustedimports/safezipfile.py#L58)
   - Don't contribute convinience functions. The goal of trustedimports is how you use the module should remain unchanged.
  
5. Add doc tests to show examples of functions that now work and which are still protected. e.g. [stdlib.rst](collective/trustedimports/stdlib.rst)

6. Install your updated version of Use your import as normal. e.g. ```import re; re.search('.*')```

7. [Raise a ticket](https://github.com/collective/collective.trustedimports/issues) to get a release of collective.trustedimports with your new import added.




