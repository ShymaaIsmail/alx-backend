#!/usr/bin/env python3
"""basic cache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching"""

    def put(self, key, item):
        """put value of a key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get a value of a key"""
        value = None
        try:
            if key:
                value = self.cache_data[key]
        except KeyError:
            return value
        return value
