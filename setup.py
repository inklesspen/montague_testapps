#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import os
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import relpath
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='montague_testapps',
    version='0.1.0',
    license='BSD',
    description='Test applications for Montague (mostly extracted from the PasteDeploy test suite)',
    long_description='%s\n%s' % (read('README.rst'), re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))),
    author='Jon Rosebaugh',
    author_email='jon@inklesspen.com',
    url='https://github.com/inklesspen/montague_testapps',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[
        "six>=1.8.0",
        "zope.interface>=4.1.1",
        "characteristic>=14.2.0",
        "webtest>=2.0.18",
    ],
    extras_require={
    },
    entry_points={
        "paste.app_factory": [
            'basic_app=montague_testapps.apps:make_basic_app',
            'other=montague_testapps.apps:make_basic_app2',
            'configed=montague_testapps.configapps:SimpleApp.make_app',
        ],
        'paste.composit_factory': [
            'remote_addr=montague_testapps.apps:make_remote_addr',
        ],
        'paste.filter_factory': [
            'caps=montague_testapps.apps:make_cap_filter',
        ],
        'paste.filter_app_factory': [
            'caps2=montague_testapps.apps:CapFilter',
        ],
        'paste.server_factory': [
            'server_factory=montague_testapps.servers.make_server_factory',
        ],
        'paste.server_runner': [
            'server_runner=montague_testapps.servers.make_server_runner',
        ],
        'montague.config_loader': [
            'testjson=montague_testapps.config:JSONConfigLoader',
        ],
    },
)
