#!/usr/bin/env python
from setuptools import setup, find_packages

required = [
    'Flask'
]

setup(
    name='demo-site',
    version='0.0.1',
    description="Demo site for Ansible demo",
    long_description='This is not really much longer...',
    include_package_data=True,
    packages='demo_site',
    zip_safe=False,
    install_requires=required,
)
