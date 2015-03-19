#!/usr/bin/env python
from math import pow
from merge_sort import timed_func

def r_sort(sequence):
    digit = 1
    while True:
        bins = [[] for i in range(10)]
        for x in sequence:
            bins[x % 10 ** digit // 10 ** digit -1].append(x)
        sequence = [number for x in bins for number in bins[x]]
        digit += 1
    return sequence
