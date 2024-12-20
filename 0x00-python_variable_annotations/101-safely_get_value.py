#!/usr/bin/env python3
"""Adding type annotations to function"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Safely return the value of a key in a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
