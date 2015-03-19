#!/usr/bin/env python
from merge_sort import timed_func

@timed_func
def r_sort(sequence):
    digit = 1
    while True:
        pos_bins = [[] for i in range(10)]
        neg_bins = [[] for i in range(10)]
        for x in sequence:
            # the expression in bins returns the number in digit place
            if x < 0:
                neg_bins[abs(x) % 10 ** digit // 10 ** (digit -1)].append(x)
            else:
                pos_bins[x % 10 ** digit // 10 ** (digit -1)].append(x)
        sequence = [number for x in neg_bins[::-1] for number in x] 
        sequence += [number for x in pos_bins for number in x]
        digit += 1
        if len(sequence) == len(pos_bins[0]) + len(neg_bins[0]):
            return sequence

if __name__ == '__main__':
    inputs = [range(500), range(1000)]
    inputs.append([10 ** 1000, 1, 2, 3, 4, 5])
    inputs.append(range(6))
    inputs.append(range(1000, 0, -1))
    inputs.append([10 ** 1000, 1, 2, 3, 4, 5] + range(1000, 0 -1))

    for inp in inputs:
        r_sort(inp)