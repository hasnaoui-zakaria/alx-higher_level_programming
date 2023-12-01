#!/usr/bin/python3

"""
- Sorting algorithms in an integers' lists
"""


def find_peak(list_of_integers):
    """
    - Checks for the peak item in a list.
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
    
