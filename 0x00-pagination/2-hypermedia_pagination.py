#!/usr/bin/env python3
"""
Hypermedia pagination
"""


import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """index_range"""
        end_index = page * page_size
        start_index = end_index - page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page"""
        data_page = []
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = self.index_range(page, page_size)
        if start <= len(self.dataset()):
            data_page = self.dataset()[start: end]
        return data_page

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_hyper"""
        page_info = {}
        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        page_info["page_size"] = len(data_page)
        page_info["page"] = page
        page_info["data"] = data_page
        page_info["next_page"] = page + 1 if page < total_pages else None
        page_info["prev_page"] = page - 1 if page >= 2 else None
        page_info["total_pages"] = total_pages
        return page_info
