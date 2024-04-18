#!/usr/bin/env python3
"""
Module for getting the first element of a sequence safely
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the sequence if it exists
    """
    if lst:
        return lst[0]
    else:
        return None
