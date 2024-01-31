#!/usr/bin/env python3
""" fifo cache module
"""

from base_caching import BaseCaching
from dataclasses import dataclass
from typing import List, Any


@dataclass
class LIFOCache(BaseCaching):

    """ Fifo cache class
    """
    # KEYS: List[str] = []

    def __post_init__(self):
        """ instance method
        """
        super().__init__()
        self._keys = []  # just for the class dsa

    def put(self, key, item) -> None:
        """ add to cache method

        Args:
            key (str): cache dict key
            item (any): key value
        """
        keys = self._keys
        if key is not None and item is not None:
            if len(self.cache_data) >= LIFOCache.MAX_ITEMS\
                    and key not in self.cache_data:
                discarded = self.cache_data.pop(keys[-1])
                print(f"DISCARD: {keys[-1]}")
                keys.pop(-1)
            keys.append(key)
            self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """ get item by key method for the cache storage

        Args:
            key (str): item key

        Returns:
            Any: item
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
