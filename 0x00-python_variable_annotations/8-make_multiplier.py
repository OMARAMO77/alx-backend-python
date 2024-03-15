#!/usr/bin/env python3
""" Complex types """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type-annotated function  "make_multiplier"
    that takes a float  multiplier  as argument and
    returns a function that multiplies a float by
    multiplier."""
    def func(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return func
