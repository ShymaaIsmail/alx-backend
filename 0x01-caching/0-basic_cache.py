#!/usr/bin/python3
""" basic cache"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching"""

    def put(self, key, item):
        """put"""
        if key and item:
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
