#!/usr/bin/python3
""" lru cache """
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache"""
    def __init__(self):
        """initialize LRUCache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        if key is None or item is None:
            return
        if key in self.cache_data:
            # Move the existing key to the end to show it was recently used
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first item (least recently used)
            discarded_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        # Move the accessed key to the end to show it was recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
