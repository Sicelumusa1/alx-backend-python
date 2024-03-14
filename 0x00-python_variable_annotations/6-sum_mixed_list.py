#!/usr/bin/env python3

"""
Defines a method that accepts a mixed list of integers and floats
and returns their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Accepts a mixed list of integers and floats and returns their sum 
    as a float

    Args:
        mxd_lst (List[Union[int, float]]): list with integers and floats.

    Returns:
        float: sum of the numbers in the list
    """
    return sum(mxd_lst)
