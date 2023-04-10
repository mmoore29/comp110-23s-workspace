"""QC04 - Dict Function Writing."""
__author__ = "730611114"


def zip(key_list: list[str], value_list: list[int]) -> dict[str, int]:
    """Produces a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list."""
    a_dict: dict[str, int] = {}
    if len(key_list) != len(value_list):
        return a_dict
    for idx in range(len(key_list)):
        a_dict[key_list[idx]] = value_list[idx]
    return a_dict