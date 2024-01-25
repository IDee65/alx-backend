#!/usr/bin/env python3
""" Hypermedia pagination """


import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """ Server class to paginate a database of popular baby names. """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Initialize instance. """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Property decorator to return the dataset. """
        return self.__dataset

    def get_dataset(self) -> List[List]:
        """ Load the dataset. """
        if self.__dataset is None:
            with open(self.DATA_FILE, "r") as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Return list of rows from dataset. """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        self.get_dataset()
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[Any, Any]:
        """ Return dictionary of pagination info """
        dataset = self.get_page(page, page_size)
        data: Dict[Any, Any] = {}
        data['page_size'] = len(dataset)
        data['page'] = page
        data['data'] = dataset
        if page > 1:
            data['prev_page'] = page - 1
        else:
            data['prev_page'] = None
        if page * page_size < len(self.__dataset):
            data['next_page'] = page + 1
        else:
            data['next_page'] = None
        data['total_pages'] = math.ceil(len(self.__dataset) / page_size)
        return data
