#!/usr/bin/env python3
""" Complex types """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A type-annotated function  sum_mixed_list
    which takes a list  mxd_lst  of integers and
    floats and returns their sum as a float. """
    return float(sum(mxd_lst))
