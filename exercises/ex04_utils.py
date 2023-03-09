"""EX04 - Computational Thinkning Practice."""
__author__ = "730611114"


def all(int_list: list[int], integer: int) -> bool:
    """Returns true if all the numbers in a list match the indicated number."""
    idx: int = 0
    i: int = 0
    if len(int_list) == 0:
        return False

    while idx < len(int_list):
        # checks to see if all the numbers in the list are eaqual to the indicated number.
        if int_list[idx] == integer:
            idx += 1
            i += 1
        else:
            idx += 1
    
    if i == len(int_list):
        return True 
    else:
        return False


def max(int_list: list[int]) -> int:
    """Returns the larges number in a list."""
    idx: int = 0
    largest_num: int = int_list[0]
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    
    while idx < len(int_list):
        # cycles integer list to find the largest number.
        if int_list[idx] > largest_num:
            largest_num = int_list[idx]
            idx += 1
        else:
            idx += 1
    return largest_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns true if two lists are eaqual to each other at every index."""
    if len(list1) != len(list2):
        return False
    
    if len(list1) == 0 and len(list2) == 0:
        return True

    idx: int = 0
    i: int = 0
    while idx < len(list1) and len(list2):
        # checks to see if the two lists are equal at each index.
        if list1[idx] == list2[idx]:
            idx += 1
            i += 1
        else:
            return False
        
    if i == len(list1) and len(list2):
        return True
    else:
        return False