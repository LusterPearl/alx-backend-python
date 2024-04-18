#!/usr/bin/env python3
"""
Module for calculating the length of elements in a list
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing each element of lst and its length.

    Args:
        lst (Iterable[Sequence]): An iterable object containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where the first element
        and the second element is the length of the sequence.
    """
    return [(i, len(i)) for i in lst]
