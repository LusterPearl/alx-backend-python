#!/usr/bin/env python3
"""
Module for converting string and int/float to tuple
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing the input string and the square of the input int/float"""
    return (k, v ** 2.0)