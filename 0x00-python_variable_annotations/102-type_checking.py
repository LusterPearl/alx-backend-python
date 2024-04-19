#!/usr/bin/env python3
"""
Module for zooming arrays
"""

from typing import Tuple, List, Any

<<<<<<< HEAD

=======
>>>>>>> 85ef8d8a8509ba37a51e3b1d025280908c92e2da
def zoom_array(lst: Tuple[Any], factor: int = 2) -> List[Any]:
    """Zooms an array by repeating each element 'factor' times"""
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
<<<<<<< HEAD
    return (zoomed_in)

=======
    return zoomed_in
>>>>>>> 85ef8d8a8509ba37a51e3b1d025280908c92e2da

array = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)