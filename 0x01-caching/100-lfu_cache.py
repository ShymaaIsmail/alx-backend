#!/usr/bin/python3
""" LFU Cache """
from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""
    def __init__(self):
        """Initialize LFUCache"""
        super().__init__()
        self.freq = defaultdict(int)  # Frequency of each key
        self.use_order = defaultdict(list)  # List of keys for each frequency
        self.key_order = []  # Order of keys by recency of use
        self.min_freq = 0

    def put(self, key, item):
        """Put item in cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and frequency
            self.cache_data[key] = item
            self._update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least frequently used item
                self._evict_least_frequent()
            # Add new item
            self.cache_data[key] = item
            self.freq[key] = 1
            self.use_order[1].append(key)
            self.key_order.append(key)
            self.min_freq = 1

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency and return the item
        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """Update the frequency of the key"""
        freq = self.freq[key]
        self.freq[key] += 1
        self.use_order[freq].remove(key)
        if not self.use_order[freq]:
            del self.use_order[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.use_order[freq + 1].append(key)

        # Move key to the end to mark it as recently used
        self.key_order.remove(key)
        self.key_order.append(key)

    def _evict_least_frequent(self):
        """Evict the least frequently used item"""
        # Find the keys with the minimum frequency
        least_freq_keys = self.use_order[self.min_freq]
        if len(least_freq_keys) == 1:
            # Only one key to evict
            key_to_evict = least_freq_keys.pop()
        else:
            # More than one key with the same minimum frequency, apply LRU
            for key in self.key_order:
                if key in least_freq_keys:
                    key_to_evict = key
                    self.key_order.remove(key)
                    break
            least_freq_keys.remove(key_to_evict)

        if not self.use_order[self.min_freq]:
            del self.use_order[self.min_freq]

        del self.cache_data[key_to_evict]
        del self.freq[key_to_evict]
        print(f"DISCARD: {key_to_evict}")

    def print_cache(self):
        """Print the cache data"""
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")
