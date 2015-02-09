def parens(input):
    sum = 0
    for char in input:
        if char == '(':
            sum += 1
        elif char == ')':
            sum -= 1
    if sum > 0:
        return 1
    elif sum < 0:
        return -1
    else:
        return 0
