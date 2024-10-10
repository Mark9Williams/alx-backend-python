#!/usr/bin/env python3
"""Zoom an array"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list with a zoomed array"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)  # Correct usage

zoom_3x = zoom_array(array, 3)  # Changed to int to match function signature
