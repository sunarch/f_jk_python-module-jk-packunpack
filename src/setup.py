################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Programming Language :: Python :: 3",
	],
	description = "Helper module to create or unpack tar archives, compress or uncompress files.",
	include_package_data = False,
	install_requires = [
		"jk_simpleexec",
		"jk_logging",
	],
	keywords = [
		"...",
	],
	license = "proprietary",
	name = "jk_packunpack",
	packages = [
		"jk_packunpack",
	],
	version = "0.2020.11.11",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)