#!/usr/bin/env python3
"""
Module for calculating the length of elements in a list
"""

from typing import Iterable, Tuple


def element_length(lst: Iterable) -> Iterable:
    """
    Returns a list of tuples containing each element of lst and its length.

    Args:
        lst (Iterable): An iterable object.

    Returns:
        Iterable: A list of tuples where the first element is an element of lst
        and the second element is the length of the element.
    """
    return [(i, len(i)) for i in lst]
