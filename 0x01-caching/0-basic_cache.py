#!/usr/bin/env python3
"""BasicCache modules"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache implements put and get methods"""
    MAX_ITEMS = None

    def put(self, key, item):
        """add an item by key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key:
            return self.cache_data.get(key)
