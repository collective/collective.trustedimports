import os
import sys

from setuptools import setup, find_packages

version = '0.1dev0'


setup(
    name='sandboxlib',
    version=version,
    description="sandboxlib whitelists a number of python functions for use "
                "in restrictedPython",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Plone',
        'Framework :: Zope2',
        'Framework :: Zope3',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    keywords='Plone sandboxlib',
    author='Jon Pentland',
    author_email='jon@iomedia.co.uk',
    url='https://github.com/collective/sandboxlib',
    license='GPL',
    package_dir={'': 'src'},
    packages=find_packages('src', exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    test_suite='i18ndude.tests',
    install_requires=[

    ]
    entry_points={

    },
)
