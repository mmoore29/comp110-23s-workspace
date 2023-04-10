"""EX05 - list utility functions."""
__author__ = "730611114"


def only_evens(int_list: list[int]) -> list:
    """When given a list of integers, return a new list of only the even integers from the given list."""
    even_list: list[int] = []
    for idx in int_list:
        if idx % 2 == 0:
            even_list.append(idx)
    return even_list 


def concat(list1: list[int], list2: list[int]) -> list:
    """When given two list of integers, returns a new list that contains all of the integers from the first list followed by all the integers from the second list."""
    list12: list[int] = []
    for idx in list1:
        list12.append(idx)
    for idx in list2:
        list12.append(idx)
    return list12


def sub(a_list: list[int], start: int, end: int) -> list:
    """When given a list of integers and a start and end index, returns a new list which is a subset of the given list, between the specified start index and the end index -1."""
    sub_list: list[int] = []
    i: int = 0
    if len(a_list) == 0 or start >= len(a_list) or end <= 0:
        return sub_list
    if start < 0:
        start = 0
    if end >= len(a_list):
        end = len(a_list)
    
    for idx in a_list:
        if i >= start and i < end:
            sub_list.append(idx)
        i += 1
    return sub_list