#!/usr/bin/env python3
"""fifo cache"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching"""

    def put(self, key, item):
        """put value of a key"""
        if key is not None and item is not None:
            if len(self.cache_data.items()) >= self.MAX_ITEMS:
                key_to_discard = (k := next(iter(self.cache_data)),
                                  self.cache_data.pop(k))
                print("DISCARD: {}".format(key_to_discard[0]))
                self.cache_data[key] = item
            else:
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
