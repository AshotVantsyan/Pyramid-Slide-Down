#!/usr/bin/env python3.8

"""
The core of the project.
Contains function which calculates the longest slide down path of the given pyramid.
"""

from typing import List

def longest_slide_down(pyramid: List[List[int]]) -> int:
    """
    The function returns the maximum path sum for the given pyramid.
    Dynamic programming purpose will be used.
    """
    best_values = dict(zip(range(len(pyramid)), [0] * len(pyramid)))
    for row in pyramid[::-1]:
        for i in range(len(row) - 1):
            best_values[i] = max(best_values[i] + row[i], best_values[i+1] + row[i+1])
    return max(best_values.values()) + row[0]