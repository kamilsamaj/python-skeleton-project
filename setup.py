#!/usr/bin/env python
from setuptools import setup, find_packages

# this setup expects you have your source code in 'src' directory
setup(
    name='_YOUR_PACKAGE_NAME_',
    use_scm_version={'write_to': 'src/_YOUR_PACKAGE_NAME_/__version__.py'},
    setup_requires=['setuptools_scm'],
    packages=find_packages('src'),
    install_requires=[
        # put the list of the required python packages here
    ],
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            '_YOUR_PACKAGE_NAME_=_YOUR_PACKAGE_NAME_.cli:cli'  # package.module:method
        ]
    }
)
