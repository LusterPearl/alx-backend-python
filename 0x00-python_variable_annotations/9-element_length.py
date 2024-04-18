#!/usr/bin/env python3
"""
Module for calculating the length of elements in a list
"""

from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing each element and its length"""
    return [(i, len(i)) for i in lst]