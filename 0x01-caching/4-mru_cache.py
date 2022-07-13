#!/usr/bin/env python3
"""MRUCache modules"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache implements put and get methods
    the caches replaces Most recently used(MRU) if full
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.recently_used = {}  # holds order of insertion 'A': index
        self.index = 0

    def put(self, key, item):
        """add an item by key"""
        if key and item:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS) and (
                    not self.cache_data.get(key)):
                least_recently_used_key = sorted(
                    self.recently_used,
                    key=lambda i: self.recently_used[i])[-1]
                self.cache_data.pop(least_recently_used_key)
                self.recently_used.pop(least_recently_used_key)
                print('DISCARD: {}'.format(least_recently_used_key))
            self.cache_data[key] = item
            self.recently_used[key] = self.index
            self.index += 1

    def get(self, key):
        """get an item by key"""
        if key:
            if key in self.recently_used:
                self.recently_used[key] = self.index
                self.index += 1
            return self.cache_data.get(key)
