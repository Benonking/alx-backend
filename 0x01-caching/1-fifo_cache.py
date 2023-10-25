#!/usr/bin/env python3
'''
Module FIFOCache
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
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

    def put(self, key, item):
        '''
        add item to cache or remove first input item if length of dict exceeds MAX_LIMIT
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        '''
            get item by key
            '''
        if key is None or key not in self.cache_dat:
            return None
        return self.cache_data.get(key, None)
