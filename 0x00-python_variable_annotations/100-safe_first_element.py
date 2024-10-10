#!/usr/bin/env python3
from typing import Any, Sequence, Optional
# The types of the elements of the input are not know


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of a list if available, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
