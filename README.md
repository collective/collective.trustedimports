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

Contents
--------

Currently support libraries which can use used without modification are:

- [stdlib supported](collective/trustedimports/stdlib.rst)
- [zipfile supported](collective/trustedimports/safezipfile.rst)
- [M2Crypto and email](collective/trustedimports/trustedemail.rst)
- [some zope/plone libraries](collective/trustedimports/plone.rst)

Contribute
----------
If you think another library should be be made importable contribute on
[github](https://github.com/collective/collective.trustedimports)

How to whitelist a module
-------------------------

1. First thing to do is decide if you can contribute to the code itself, then perhaps the best place is to submit a patch to your thirdparty code to allow it to be imported in restricted python.

2. Next determine if the module is safe. Things you should look for are: 
   - Does any function involve writing or reading from files?
   - Does any function reveal sensitive system information?
   - Does any function have the capacity to block or take a long time?
   - Does any function make network calls?
   
3. Find a place in trusedimports for your whitelist. e.g. [stdlib.py](collective/trustedimports/stdlib.py)

4. Add your whitelist
   - Only whitelist functions that are safe.
   - you can use our [convenience function](https://github.com/collective/collective.trustedimports/blob/master/collective/trustedimports/util.py#L9) to handle whitelisting in both zope.security and Products.PythonScripts at the same time (there are two different systems of restricted python).
   - If what you want to whitelist does include unsafe calls such as access to the filesystem, there are [ways to monkey patch to make it safe](https://github.com/collective/collective.trustedimports/blob/master/collective/trustedimports/safezipfile.py#L58)
   - Don't contribute convinience functions. The goal of trustedimports is how you use the module should remain unchanged.
  
5. Add doc tests to show examples of functions that now work and which are still protected. e.g. [stdlib.rst](collective/trustedimports/stdlib.rst)

6. Install your updated version of Use your import as normal. e.g. ```import re; re.search('.*')```

7. [Raise a ticket](https://github.com/collective/collective.trustedimports/issues) to get a release of collective.trustedimports with your new import added.




