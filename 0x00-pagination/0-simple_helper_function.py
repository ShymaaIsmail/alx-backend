#!/usr/bin/env python3
"""
Simpler Helper
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range"""
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
