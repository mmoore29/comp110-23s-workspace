"""EX07 - Practice with some dictionary functions."""
__author__ = "730611114"


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary that inverts the keys and values of the original."""
    inv_dict: dict[str, str] = {}

    for key in a_dict:
        # checking if any of the values in a_dict match any of the keys in inv_dict
        if a_dict[key] in inv_dict:
            raise KeyError("Duplicate Keys")
        inv_dict[a_dict[key]] = key
    return inv_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns a str which is the color that appears most frequently."""
    max_count: int = 0
    favorite_color: str = ""
    color_count: dict[str, int] = {}
    for key in color_dict:
        color = color_dict[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    for key in color_count:
        if color_count[key] > max_count:
            max_count = color_count[key]
            favorite_color = key 
    return favorite_color


def count(a_list: list[str]) -> dict[str, int]:
    """Returns a dict where each key is a unique value in the input list and each value associated is the count of the number of times that value appeared in the input list."""
    a_dict: dict[str, int] = {}
    i: int = 0
    while i < len(a_list):
        key = a_list[i]
        if key in a_dict:
            a_dict[key] += 1
        else:
            a_dict[key] = 1
        i += 1
    return a_dict