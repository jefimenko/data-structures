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
    for ind, num in enumerate(sequence):
        # base case
        if len(sequence) <= 1:
            return sequence
        # recursive case
        middle = len(sequence) / 2
        left = merge_sort(sequence[:middle])
        right = merge_sort(sequence[middle:])

        return merge(left, right)


def merge(left, right):
    result =[]
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
            result.append(left.pop(0))
    while right:
            result.append(right.pop(0))
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
    merge_sort(something_else)