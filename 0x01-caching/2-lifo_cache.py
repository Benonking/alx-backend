#!/usr/bin/env python3
'''
Module LIFOCache
'''
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    Class FIFOCache implements methods:
    put -> add item to cache if atems in cahec is greather that BaseCaching,
                            remove first item that was input
    get
    '''

    def __init__(self):
        '''
        Initialise class
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''
        add item to cache or remove first input item if
            length of dict exceeds MAX_LIMIT
        '''
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                popped_item = self.cache_data.popitem()
                print(f"DISCARD: {popped_item[0]}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''
          get item by key
        '''
        return self.cache_data.get(key, None)
