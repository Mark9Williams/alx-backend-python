#!/usr/bin/env python3
"""Validated a piece of code and applied modifications"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list with a zoomed array"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Convert array to a tuple

zoom_2x = zoom_array(array)  # Correct usage

zoom_3x = zoom_array(array, 3)  # Correct usage
