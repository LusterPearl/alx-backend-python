#!/usr/bin/env python3
"""
Module for safely getting a value from a dictionary
"""

from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any,
    default: Union[T, None] = None
) -> Union[T, Any]:
    """
    Returns the value associated with the key in the dictionary if it exists
    """
    if key in dct:
        return dct[key]
    else:
        return default
