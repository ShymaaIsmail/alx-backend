#!/usr/bin/env python3
"""FIFO Cache System"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching"""

    def __init__(self):
        """Initialize FIFOCache class"""
        super().__init__()

    def put(self, key, item):
        """Put value of a key"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.cache_data:
                    key_to_discard = next(iter(self.cache_data))
                    self.cache_data.pop(key_to_discard)
                    print("DISCARD: {}".format(key_to_discard))
            self.cache_data[key] = item

    def get(self, key):
        """Get a value of a key"""
        return self.cache_data.get(key, None)
