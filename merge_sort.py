#!/usr/bin/env python
import time
import random


def timed_func(func):
    """Decorator for timing our traversal methods."""
    def timed(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print "time expired: %s" % elapsed
        return result
    return timed


@timed_func
def time_merge_sort(sequence):
    return merge_sort(sequence)


def merge_sort(sequence):
    """Mergesort."""
    # base case
    if len(sequence) <= 1:
        return sequence

    # recursive case
    middle = len(sequence) // 2
    left = merge_sort(sequence[:middle])
    right = merge_sort(sequence[middle:])

    return merge(left, right)


def merge(left, right):
    result = []
    l_index, r_index = 0, 0
    l_end, r_end = len(left), len(right)
    while l_index < l_end and r_index < r_end:
        if left[l_index] <= right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
    if l_index < l_end:
        result.extend(left[l_index:])
    if r_index < r_end:
        result.extend(right[r_index:])
    return result

if __name__ == "__main__":
    # in order
    something = [x for x in range(1000)]
    time_merge_sort(something)
    # reverse order
    something_else = [x for x in range(1000, 0, -1)]
    time_merge_sort(something_else)
    # x10
    something_else = [x for x in range(10000)]
    time_merge_sort(something_else)
    # x100
    something_else = [x for x in range(100000)]
    random.shuffle(something_else)
    time_merge_sort(something_else)