"""EX05 utils unit tests."""
__author__ = "730611114"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

#only_evens use case test #1.
def test_only_evens() -> None:
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]

#only_evens use case test #2.
def test_only_evens_empty() -> None:
    test_list: list[int] = []
    assert only_evens(test_list) == []

#only_evens use case test #3.
def test_only_evens_one_element() -> None:
    test_list: list[int] = [3]
    assert only_evens(test_list) == []

#only_evens edge case test #4.
def test_only_evens_negative() -> None:
    test_list: list[int] = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
    assert only_evens(test_list) == [-4, -2, 0, 2, 4]

#concat use case test #1.
def test_concat() -> None:
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6]

#concat use case test #2.
def test_concat_empty() -> None:
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []

#concat use case test #3.
def test_concat_one_element() -> None:
    test_list1: list[int] = [2]
    test_list2: list[int] = [6]
    assert concat(test_list1, test_list2) == [2, 6]

#concat use case test #4.
def test_concat_negatives() -> None:
    test_list1: list[int] = [-1, -2, 0]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [-1, -2, 0, 4, 5, 6]

#sub use case test #1.
def test_sub() -> None:
    test_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(test_list, start, end) == [20, 30]

#sub use case test #2.
def test_sub_empty() -> None:
    test_list: list[int] = []
    start: int = 1
    end: int = 3
    assert sub(test_list, start, end) == []

#sub use case test #3.
def test_sub_inex_too_big() -> None:
    test_list: list[int] = [10, 20, 30, 40]
    start: int = 4
    end: int = 3
    assert sub(test_list, start, end) == []

#sub edge case test #4.
def test_sub_negative_index() -> None:
    test_list: list[int] = [10, 20, 30, 40]
    start: int = -5
    end: int = 3
    assert sub(test_list, start, end) == [10, 20, 30]