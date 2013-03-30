#!/usr/bin/env python
#coding: utf-8

from setuptools import setup

setup(
	name = "messytables-jts",
	author = "Martin Keegan",
	author_email = "martin.keegan@okfn.org",
	version = "0.3",
	license = "Apache Licence v2.0",
	url = "",
	download_url = "",
	description = "Python library for mapping Messytable cell types to strings",
	py_modules = ["messytables_jts"],
	install_requires = ["messytables", "json-table-schema"],
	scripts = ["bin/csv2jts"] 
)
