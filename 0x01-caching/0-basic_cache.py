#!/usr/bin/env python3
""" Basic cache module
"""

from base_caching import BaseCaching
from typing import Any
from dataclasses import dataclass


class BasicCache(BaseCaching):

    """ Base cache class
    """

    def __init__(self) -> None:
        """ instance method
        """
        super().__init__()

    def put(self, key: str, item: Any) -> None:
        """ put method to add item to the cache data storage

        Args:
            key (str): Item key
            item (Any): Item to be added
        """
        if key is not None and item is not None:
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
