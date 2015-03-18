def q_sort(sequence): 
    if len(sequence) == 1:
        return 
    pivot = get_pivot(sequence)
    left = []
    right = []
    for item in sequence:
        if item > pivot and item is not pivot:
            right.append(item)
        else:
            left.append(item)
    right = q_sort(right)
    left = q_sort(left)

    if len(sequence) > 2:
        return left + [pivot] + right
    else:
        return left + right

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
