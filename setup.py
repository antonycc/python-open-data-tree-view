#!/usr/bin/env python3
# Purpose: install local dependencies and apply local configuration changes
# See:
#    https://docs.python.org/3/distutils/setupscript.html#setup-script
#    https://pypi.python.org/pypi?%3Aaction=list_classifiers
# Usage:
#    prepare source distribution:
#       python3 setup.py sdist
#    initialise local distribution:
#       python3 -m pip install .
#    initialise local distribution (distutils, does not pick up `install_requires`):
#       python3 setup.py install
# https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
# https://python-packaging.readthedocs.io/en/latest/minimal.html

import sys
from distutils.core import setup
from pathlib import Path

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)
if CURRENT_PYTHON < REQUIRED_PYTHON:
   sys.stderr.write('CURRENT_PYTHON: {} REQUIRED_PYTHON: {}'.format(REQUIRED_PYTHON, CURRENT_PYTHON))
   sys.exit(1)

requirements_dot_txt = Path('./requirements.txt').read_text().split('\n')
modules = list(filter(lambda x: x and not x.startswith('#'), requirements_dot_txt))
setup(name='Tree View',
      version='0.0.1',
      description='A demonstration of individual building data combined with open data',
      license='MIT',
      author='Antony Cartwright',
      author_email='antonyccartwright@gmail.com',
      url='https://polycode.co.uk/',
      download_url='https://github.com/antonycc/python-open-data-tree-view',
      install_requires=modules,
      zip_safe=False,
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Console',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python :: 3.6',
          'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
          'Topic :: Scientific/Engineering :: Information Analysis'
          ],
     )

