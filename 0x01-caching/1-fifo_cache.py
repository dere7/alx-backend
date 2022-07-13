#!/usr/bin/env python3
"""FIFOCache modules"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache implements put and get methods
    the caches replaces the block in order they were added
    i.e. The first item to be inserted will be the first to be
    replaced when the cache is full
    """

    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """add an item by key"""
        if key and item:
            if (len(self.cache_data) >= BaseCaching.MAX_ITEMS) and (
                    not self.cache_data.get(key)):
                discarded_key = self.queue[0]
                self.queue.remove(discarded_key)
                self.cache_data.pop(discarded_key)
                print('DISCARD: {}'.format(discarded_key))
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key:
            return self.cache_data.get(key)
