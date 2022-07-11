#!/usr/bin/env python3
"""helper utility function for pagination"""
from typing import Tuple


def index_range(page: int, page_size) -> Tuple[int, int]:
    """returns tuple of start and end index range for given paga number
    and size"""
    start_index = (page - 1) * page_size
    end_index = page_size * page
    return start_index, end_index
