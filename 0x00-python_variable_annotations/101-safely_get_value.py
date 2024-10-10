#!/usr/bin/env python3
"""Safely get the value"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')  # A generic type variable for values


def safely_get_value(
        dct: Mapping[Any, T],
        key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """ Return the value linked to key in dct if it exists"""
    if key in dct:
        return dct[key]
    else:
        return default
