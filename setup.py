#!/usr/bin/env python

from distutils.core import setup

long_desc = 'Licensed under the generic MIT License.\"fresh-baked-pi\" can either be downloaded from the ' \
            'Releases page on GitHub and manually added to PATH or installed via \"pip\".'
version = ''

with open("version.txt", "r", encoding="utf-8") as fh:
    version = fh.read()
    fh.close()

setup(name='fresh-baked-pi',
      version=version,
      py_modules=['fresh-baked-pi'],
      description='Fresh Baked Pi | The RPi Setup Utility',
      long_description=long_desc,
      long_description_content_type='text/markdown',
      author='Tushar Iyer',
      author_email='',
      url='https://github.com/tushariyer/fresh-baked-pi',
      project_urls={
              "Bug Tracker": "https://github.com/tushariyer/fresh-baked-pi/issues",
          }
      )
