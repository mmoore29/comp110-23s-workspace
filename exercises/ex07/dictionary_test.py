"""EX07 dictionary unit test."""
__author__ = "730611114"


from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


# invert use case test 1.
def test_invert_normal() -> None:
    """Tests normal dict."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


# invert use case test 2.
def test_invert_colors() -> None:
    """Tests dict with duplicate values."""
    test_dict: dict[str, str] = {'red': '1', 'blue': '2'}
    assert invert(test_dict) == {'1': 'red', '2': 'blue'}


# invert edge case test 3.
def test_invert_empty() -> None:
    """Tests empty dict."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


# favorite_color use case test 1.
def test_favorite_color() -> None:
    """Tests normal dict."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "blue"


# favorite_color use case test 2.
def test_favorite_color_empty() -> None:
    """Tests empty dict."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


# favorite_color edge case test 3.
def test_favorite_color_tie() -> None:
    """If there is a tie for most popular color, return the color that appeared in the dictionary first."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "joe": "red", "bob": "red"}
    assert favorite_color(test_dict) == "blue"


# count use case test 1.
def test_count_normal() -> None:
    """Tests normal list."""
    test_list: list[str] = ['a', 'b', 'a', 'c']
    assert count(test_list) == {'a': 2, 'b': 1, 'c': 1}


# count use case test 2.
def test_count_colors() -> None:
    """Tests normal use case test with colors."""
    test_list: list[str] = ['red', 'blue', 'green', 'red']
    assert count(test_list) == {'red': 2, 'blue': 1, 'green': 1}


# count use edge test 3.
def test_count_empty() -> None:
    """Tests empty list."""
    test_list: list[str] = []
    assert count(test_list) == {}