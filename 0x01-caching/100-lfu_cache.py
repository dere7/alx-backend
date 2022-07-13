#!/usr/bin/env python3
"""LFUCache modules"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFUCache implements put and get methods
    the caches replaces Least Frequently Used(MFU) if full
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        # holds frequency of usage
        self.frequently_used = {}
        self.recently_used = {}
        self.index = 0

    def get_lfu_key(self):
        """gets least frequently used key"""
        min_key = min(self.frequently_used,
                      key=lambda i: self.frequently_used[i])
        min_freq = self.frequently_used[min_key]
        lfu_keys = [
            k for k in self.frequently_used
            if self.frequently_used[k] == min_freq]
        if len(lfu_keys) == 1:
            return lfu_keys[0]
        filtered_ru = {k: v for k, v in self.recently_used.items()
                       if k in lfu_keys}
        return min(filtered_ru, key=lambda i: filtered_ru[i])

    def put(self, key, item):
        """add an item by key"""
        if key and item:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS) and (
                    not self.cache_data.get(key)):
                lfu_key = self.get_lfu_key()
                self.cache_data.pop(lfu_key)
                self.frequently_used.pop(lfu_key)
                self.recently_used.pop(lfu_key)
                print('DISCARD: {}'.format(lfu_key))
            if key in self.cache_data:
                self.frequently_used[key] += 1
            else:
                self.frequently_used[key] = 0
            self.cache_data[key] = item
            self.recently_used[key] = self.index
            self.index += 1

    def get(self, key):
        """get an item by key"""
        if key:
            if key in self.frequently_used:
                self.frequently_used[key] += 1
            if key in self.recently_used:
                self.recently_used[key] = self.index
                self.index += 1
            return self.cache_data.get(key)
