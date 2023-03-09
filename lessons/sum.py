"""Example function for unit test"""

def sum(xs: list[float]) -> float:
    """return the sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    #while idx < len(xs):
    #   sum_total += xs[idx]
    #    idx += 1
    #return sum_total

    #for item in xs:
    #   sum_total += item
    #return sum_total

    for item in range(0, len(xs)):
        sum_total += xs[item]
    return sum_total