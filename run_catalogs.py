# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:43:21 2020

@author: au195407
"""

import argparse
import logging
from flows.catalogs import get_catalog, download_catalog, get_catalog_missing

if __name__ == '__main__':
	# Parse command line arguments:
	parser = argparse.ArgumentParser(description='Run catalog.')
	parser.add_argument('-d', '--debug', help='Print debug messages.', action='store_true')
	parser.add_argument('-q', '--quiet', help='Only report warnings and errors.', action='store_true')
	args = parser.parse_args()

	# Set logging level:
	logging_level = logging.INFO
	if args.quiet:
		logging_level = logging.WARNING
	elif args.debug:
		logging_level = logging.DEBUG

	# Setup logging:
	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
	console = logging.StreamHandler()
	console.setFormatter(formatter)
	logger = logging.getLogger('flows')
	if not logger.hasHandlers():
		logger.addHandler(console)
	logger.setLevel(logging_level)

	for targetid in get_catalog_missing():
		logger.info("Downloading catalog for targetid=%d...", targetid)
		download_catalog(targetid)

	cat = get_catalog(2)
	print(cat)
