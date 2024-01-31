#!/usr/bin/env python3
""" LFU cache module
"""

from base_caching import BaseCaching
from dataclasses import dataclass
from typing import Any, Union


@dataclass
class LFUCache(BaseCaching):

    """ LFU cache class
    """

    def __post_init__(self):
        """ instance method
        """
        super().__init__()
        self._freq = {}  # Dictionary to store frequency of each item
        self._count = 0

    def get_least_frequent_key(self) -> Union[None, str]:
        """ gets the least frequently used key

        Returns:
            None | str: key or None if key couldn't not get key
        """
        least_freq = min(self._freq.values())
        # print(self._freq.items())
        for key, freq in self._freq.items():
            if freq == least_freq:
                return key
        return None

    def put(self, key: str, item: Any) -> None:
        """ add to cache method

        Args:
            key (str): cache dict key.
            item (Any): key value
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS \
                    and key not in self.cache_data:
                least_freq_key = self.get_least_frequent_key()
                if least_freq_key:
                    self.cache_data.pop(least_freq_key)
                    self._freq.pop(least_freq_key)
                    print(f"DISCARD: {least_freq_key}")
            self.cache_data[key] = item
            if key in self._freq:
                self._freq[key] += 1
            else:
                self._freq[key] = 1

    def get(self, key: str) -> Any:
        """ get item by key method for the cache storage

        Args:
            key (str): item key

        Returns:
            Any: item
        """
        if key is not None:
            if key in self.cache_data:
                self._freq[key] += 1  # Increment the frequency
                return self.cache_data[key]
        return None
