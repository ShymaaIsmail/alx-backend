#!/usr/bin/env python3
""" basic cache"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching"""


    def put(self, key, item):
        """put"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get"""
        return self.cache_data.get(key, None)
