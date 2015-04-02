from merge_sort import timed_func


def q_sort(sequence):
    if len(sequence) <= 1:
        # Return a sequence of one sorted item, or stop if no input
        return sequence
    if len(sequence) == 2:
        # Return a sequence of two sorted items
        if sequence[1] > sequence[0]:
            return sequence
        else:
            return sequence[::-1]
    pivot = get_pivot(sequence)
    left = []
    right = []
    center = []
    for index, item in enumerate(sequence):
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            center.append(item)
    return q_sort(left) + center + q_sort(right)


def get_pivot(sequence):
    first = sequence[0]
    last = sequence[-1]
    mid_index = len(sequence) // 2
    middle = sequence[mid_index]

    if last > first > middle or middle > first > last:
        return first
    if last > middle > first or first > middle > last:
        return middle
    return last



@timed_func
def timed_q_sort(sequence):
    return q_sort(sequence)


def same_maker(how_many):
    moAr = []
    for each in range(how_many):
        moAr.append(1)
    return moAr


if __name__ == '__main__':
    inputs = [range(500), range(1000)]
    inputs.append(same_maker(500))
    inputs.append(same_maker(997))

    for inp in inputs:
        timed_q_sort(inp)
