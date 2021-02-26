from setuptools import setup, find_packages
from sys import platform
import os

required_packages = [
    'omc>=0.2.3'
]
setup(
    name="omcm",
    version="0.0.1",
    author="ganlin lu",
    author_email="linewx1981@gmail.com",
    description="omc mger",
    license="",
    keywords="",
    url="https://github.com/linewx/omcm",
    long_description="omc manager",
    long_description_content_type='text/markdown',
    packages = find_packages(exclude=['tests', 'docs']),
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'omcm = omcm.main:main',
        ],
    },
    install_requires=required_packages,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

)