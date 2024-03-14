#!/usr/bin/env python3

"""
Retuns a function that multiples a float by the given multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Retuns a function that multiples a float by the given multiplier

    Args:
        multiplier(float): The multiplier value

    Returns:
        Callable[[float], float]: A function that takes a float and returns 
        the product
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
