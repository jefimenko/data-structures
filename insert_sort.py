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
def insert_sort(sequence):
    """Insert sort with small optimization for best case."""
    for ind, num in enumerate(sequence):
        # Move number to appropriate place
        while ind > 0:
            if num > sequence[ind - 1]:
                break
            if num < sequence[ind - 1]:
                sequence[ind], sequence[ind - 1] = sequence[ind - 1], sequence[ind]
            ind -= 1
    return sequence

if __name__ == "__main__":
    something = [x for x in range(1000)]
    insert_sort(something)
    something_else = [x for x in range(10000)]
    insert_sort(something_else)
    something_else = [x for x in range(1000, 0, -1)]
    insert_sort(something_else)
    something_else = [x for x in range(2000, 0, -1)]
    insert_sort(something_else)
    something_else = [x for x in range(1000)]
    random.shuffle(something_else)
    insert_sort(something_else)