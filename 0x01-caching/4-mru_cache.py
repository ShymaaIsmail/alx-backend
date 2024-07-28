#!/usr/bin/python3
""" mru cache """
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """mruCache class"""
    def __init__(self):
        """initialize mruCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put item in cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            # Move the existing key to the end to show it was recently used
            self.cache_data.move_to_end(key, last= False)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first item (most recently used)
            discarded_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """get item in cache"""
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the beginning to show it was recently used
        self.cache_data.move_to_end(key, last= False)
        return self.cache_data[key]
