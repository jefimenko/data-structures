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
    for item in sequence:
        if item > pivot[0] and item is not pivot[0]:
            right.append(item)
        elif item is not pivot[0]:
            left.append(item)

    return q_sort(left)+ pivot + q_sort(right)

def get_pivot(sequence):
    first = sequence[0]
    last = sequence[-1]
    mid_index = len(sequence) // 2
    middle = sequence[mid_index]

    if last > first > middle or middle > first > last:
        return [first]
    if last > middle > first or first > middle > last:
        return [middle]
    return [last]
