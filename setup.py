#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name='MCKLD',
	version='0.1',
	description='estimate the relative entropy',
	long_description_content_type="text/markdown",
	authors='Ahmad Mehrabi, Abolfazl Ahmadi Rahmat',
	url='https://github.com/ahmadiphy/MCKLdivergence',
	packages=[],
	scripts=['MCKLD.py','MCKLD_parallelERE.py'],
	install_requires=['MCEvidence'],
	)
