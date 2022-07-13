#!/usr/bin/env python3
"""LIFOCache modules"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache implements put and get methods
    the caches replaces the block added most recently first
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.recently_added = None

    def put(self, key, item):
        """add an item by key"""
        if key and item:
            if (len(self.cache_data) == BaseCaching.MAX_ITEMS) and (
                    not self.cache_data.get(key)):
                self.cache_data.pop(self.recently_added)
                print('DISCARD: {}'.format(self.recently_added))
            self.cache_data[key] = item
            self.recently_added = key

    def get(self, key):
        """get an item by key"""
        if key:
            return self.cache_data.get(key)
