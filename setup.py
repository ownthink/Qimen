#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup

setup(name='qimen',
      version='0.1.0',
      description='Qimen Natural Language Processing',
      author='Yener(Zheng Wenyu)',
      author_email='help@ownthink.com',
      url='https://github.com/ownthink/Qimen',
      license='MIT',
      # install_requires=['', ''],
      packages=['qimen'],
      package_dir={'qimen': 'qimen'},
      package_data={'qimen': ['*.*', 'data/*']}
      )
