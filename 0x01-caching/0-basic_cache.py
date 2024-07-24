#!/usr/bin/env python3
"""basic cache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching"""

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data` the
           `item` value for the key `key`
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get"""
        value = None
        try:
            if key:
                value = self.cache_data[key]
        except KeyError:
            return value
        return value
