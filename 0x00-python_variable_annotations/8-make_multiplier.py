#!/usr/bin/env python3
"""
Module for creating a multiplier function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the given multiplier"""
    def multiplier_function(x: float) -> float:
        """Returns the result of multiplying x by the multiplier"""
        return x * multiplier
    return multiplier_function