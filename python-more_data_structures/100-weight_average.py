#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Calculates the weighted average of a list of tuples.

    Args:
        my_list: A list of tuples, where each tuple contains (score, weight).

    Returns:
        The weighted average, or 0 if the list is empty.
    """
    if not my_list:
        return 0

    total_weighted_sum = 0
    total_weight = 0

    for score, weight in my_list:
        total_weighted_sum += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    return total_weighted_sum / total_weight
