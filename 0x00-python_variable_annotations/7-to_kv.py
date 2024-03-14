#!/usr/bin/env python3

"""
Converts a string and an int/float to a tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and an int/float to a tuple

    Args:
        k (str): Input string
        v ([int, float]): Input int or float

    Returns:
        Tuple[str, float]: A tuple with the string `k` and the 
        square of `v`
    """
    return k, v ** 2.0
