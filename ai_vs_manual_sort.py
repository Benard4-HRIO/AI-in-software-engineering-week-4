from operator import itemgetter


def sort_dicts_by_key(data, key, reverse=False):
    """
    AI-suggested approach: use Python's built-in sorted with itemgetter.
    Stable, fast, and memory-efficient (Timsort, implemented in C).

    :param data: List[Dict]
    :param key: Hashable key present in each dict
    :param reverse: Whether to sort in descending order
    :return: New sorted list
    """
    return sorted(data, key=itemgetter(key), reverse=reverse)


def merge_sort_dicts(data, key, reverse=False):
    """
    Manual implementation: stable mergesort in pure Python for comparison.

    :param data: List[Dict]
    :param key: Hashable key present in each dict
    :param reverse: Whether to sort in descending order
    :return: New sorted list
    """
    if len(data) <= 1:
        return data[:]

    midpoint_index = len(data) // 2
    left_half = merge_sort_dicts(data[:midpoint_index], key, reverse)
    right_half = merge_sort_dicts(data[midpoint_index:], key, reverse)

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        left_value = left_half[left_index][key]
        right_value = right_half[right_index][key]

        # Stable: prefer left element on ties
        if (left_value <= right_value) ^ reverse:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    if left_index < len(left_half):
        merged.extend(left_half[left_index:])
    if right_index < len(right_half):
        merged.extend(right_half[right_index:])

    return merged


__all__ = [
    "sort_dicts_by_key",
    "merge_sort_dicts",
]


