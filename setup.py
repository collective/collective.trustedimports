# -*- coding: utf-8 -*-
"""Installer for the collective.sandboxlib package."""

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
    version='0.1',
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
    url='http://pypi.python.org/pypi/restrictedpytonlib',
    license='GPL',
    packages=find_packages('collective.trustedimports', exclude=['ez_setup']),
#    namespace_packages = ['collective'],
    package_dir={'': '.'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'AccessControl',
          'zope.security',
          'zope.configuration',
          'zope.untrustedpython',

    ],
    extras_require={
        'test': [
#            'plone.app.testing',
#            'plone.app.contenttypes',
#            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
