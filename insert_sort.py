def sort(sequence):
    for ind, num in enumerate(sequence):

        # Move number to appropriate place
        while ind > 0:
            if num < sequence[ind - 1]:
                sequence[ind], sequence[ind - 1] = sequence[ind - 1], sequence[ind]
            ind -= 1

    return sequence


if __name__ == "__main__":
    something = [x for x in range(100)]
    print sort(something)
    something_else = [x for x in range(1000, 0, -1)]
    print sort(something_else)