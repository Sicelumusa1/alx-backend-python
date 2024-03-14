#!/usr/bin/python3

"""
Defines suming up of float numbers in input list
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums up the float numbers in the input list

    Args:
        input_list (List[float]): List of float numbers

    Returns:
        float: Sum of the float numbers in the list
    """
    return sum(input_list)
