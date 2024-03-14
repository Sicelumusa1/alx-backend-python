#!/usr/bin/env python3

"""
Returns a list of tuples containing each element from the input list
along with its length
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Returns a list of tuples containing each element from the input list
    along with its length

    Args:
        lst (List[str]): Input list of string

    Returns:
        List[Tuple[str, int]]: List of tuples where the first element 
        is a string from the input list and the second element is its length
    """
    return [(i, len(i)) for i in lst]
