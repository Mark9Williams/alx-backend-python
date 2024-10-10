#!/usr/bin/env python3

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with a string and an int"""
    return (k, float(v * v))
