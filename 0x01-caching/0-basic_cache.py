#!/usr/bin/env python3
'''
BaseCaching Module
'''
BaseCaching = __import__('BaseCaching').BaseCaching


class BasicCache (BaseCaching):
    '''
    BasicCache Defines methods:
    put -> add item to cache
            get -> get item from cache
    '''

    def __init__(self):
        '''
        initialisse super class in child class
        '''
        super().__init__()

    # super self.cache_data
    def put(self, key, item):
        '''
        add item to cache dictionary
        '''
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        '''
        get item by key
        '''
        return self.cache_data.get(key, None)
