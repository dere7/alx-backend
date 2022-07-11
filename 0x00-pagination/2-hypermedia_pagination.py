#!/usr/bin/env python3
"""simple pagination implementation"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size) -> Tuple[int, int]:
    """returns tuple of start and end index range for given paga number
    and size"""
    start_index = (page - 1) * page_size
    end_index = page_size * page
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get page returns a data for specified page and page size"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        return self.dataset()[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns the dictionary that contains data and hypermedias"""
        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset())/page_size)
        return {
            'page_size': len(dataset_page),
            'page': page,
            'data': dataset_page,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
