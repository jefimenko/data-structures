#!/usr/bin/env python
from merge_sort import timed_func

@timed_func
def r_sort(sequence):
    digit = 1
    while True:
        bins = [[] for i in range(10)]
        for x in sequence:
            bins[x % 10 ** digit // 10 ** digit -1].append(x)
        sequence = [number for x in bins for number in bins[x]]
        digit += 1
        if len(sequence) == len(bins[0]):
            return sequence


if __name__ == '__main__':
    inputs = [range(500), range(1000)]


    for inp in inputs:
        r_sort(inp)