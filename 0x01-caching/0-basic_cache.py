#!/usr/bin/env python3
'''
BaseCaching Module
'''
from BaseCaching import BaseCaching
#BaseCaching = __import__('BaseCaching').BaseCaching


class BasicCache (BaseCaching):
    '''
    BasicCache Defines methods:
    put -> add item to cache
            get -> get item from cache
    '''
    # super self.cache_data
    def put(self, key, item):
        '''
        add item to cache dictionary
        '''
        if key is None or item is None:
            return
       
        self.cache_data[key] = item

    def get(self, key):
        '''
        get item by key
        '''
        return self.cache_data.get(key, None)
