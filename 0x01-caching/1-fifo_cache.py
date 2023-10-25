#!/usr/bin/env python3
'''
Module FIFOCache
'''
BaseCaching = __import__('BaseCaching').BaseCaching
class FIFOCache(BaseCaching):
	'''
	Class FIFOCache implements methods:
	put -> add item to cache if atems in cahec is greather that BaseCaching,
				remove first item that was input
	get
	'''
	def __init__ (self):
		super().__init__()
	def put(self, key, item):
