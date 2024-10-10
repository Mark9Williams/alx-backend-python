#!/usr/bin/env python3

from typing import List, Tuple, Any


def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    return [(i, len(i)) for i in lst]
