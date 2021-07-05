# -*- coding: utf-8 -*-
"""Installer for the collective.trsutedimports package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.md').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='collective.trustedimports',
    version='0.2dev',
    description="RestrictedPython provides a restricted execution environment "
                "for Python, e.g. for running untrusted code. This package "
                "allows a number of trusted modules to run in this restricted "
                "environment. RestrictedPython is used in zope.untrustedpython, "
                "Plone, Plomino and Rapido amoung others.",

    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3.6",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Python Plone',
    author='PretaGov',
    author_email='software@pretaweb.com',
    url='http://pypi.python.org/pypi/trustedimports',
    license='GPL',
    packages=find_packages(),
    namespace_packages = ['collective'],
    #package_dir={'': '.'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'AccessControl',
          'zope.security',
          'zope.configuration',
          'zope.untrustedpython',
        'requests',
    ],
    extras_require={
        'test': [
            #'defusedxml', #TODO need to add tests for this
            'collective.taskqueue',
            'lxml', # TODO need to add tests for this
            'pystache', #TODO need to add tests for this
            #'M2Crypto' #TODO need to add tests for this
            'phonenumbers', #TODO need to add tests for this
            'zeep',
            'Plone',
            'plone.api',
            'collective.taskqueue',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
