#!/usr/bin/env python3
"""annotating parameters and return values with the appropriate types"""

from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """Returns a list with the length of each element"""
    return [(i, len(i)) for i in lst]
