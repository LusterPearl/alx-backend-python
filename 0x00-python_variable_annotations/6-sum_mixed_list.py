#!/usr/bin/env python3
"""
Module for summing a list of mixed integers and floats
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of mixed integers and floats"""
    return sum(mxd_lst)