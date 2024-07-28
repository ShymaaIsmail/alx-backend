#!/usr/bin/python3
""" MRU Cache """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""
    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Put item in cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the key from the current position in order list
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the most recently used item
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add the key to the cache and update the order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as most recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
