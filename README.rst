sandboxlib
==========

.. contents::


Introduction
------------

This package whitelists a number of common Python packages for use in restrictedPython. 
It also contains special versions of some libraries that have been altered to remove filesystem access to make them secure.

It is designed to be a single download to give your zope/plone instance access to a lot more power TTW from tools such as 
Plomino, PloneFormGen, collective.listingviews and other addons that allow power plone development.

Contents
--------

Currently support librires which can use used without modification are:

- email.mime: To allow sending email with attachments and HTML
- M2Crypto: allowing encrypting and signing of mail messages via smime


