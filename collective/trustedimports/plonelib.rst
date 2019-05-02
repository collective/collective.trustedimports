Plonelib
========

#TODO: these should be moved into Plone itself


plone.subrequest
----------------

Usecase: Make our own subrequests


#TODO write test

plone.api
---------

>>> teval("from plone.api.portal import get_tool")

#TODO: write test

plone.protect
-------------

It's possible to disable CSRF protection on a request

>>> teval("from plone.protect.interfaces import IDisableCSRFProtection;from zope.interface import alsoProvides")

or for a single object

>>> teval("from plone.protect.utils import safeWrite")

plone.app.textfield
-------------------

It's useful to be able to access RichTextValue

#>>> teval("from plone.app.textfield.value import RichTextValue; v = RichTextValue('')")

#TODO: write test


Products.PortalTransforms
-------------------------

Usecase: Do transforms in restricted python

#TODO: write test

plone.namedfile
---------------

Usecase: Access a blob files data from restricted python

#TODO: write test

plone.namedfile.file.NamedBlobFile

