def balanceness(paren_series):
    indicator = 0
    for paren in paren_series:
        print paren
        if paren == u'(':
            indicator += 1
        elif paren == u')':
            indicator -= 1

        # At any point in time, if a ')' precedes a '(', then the series
        # of parenthesis is broken, and the rest of the string does not need
        # to be traversed.
        if indicator < 0:
            return -1

    # If the indicator has remained greater than or equal to 0 the whole
    # traversal of the string, then no ')'s have preceded unclosed '('s.
    if indicator is 0:
        # An indicator = 0 means an equal number of '('s and ')'s.
        return 0
    else:
        # An indicator > 1 means a greater number of '('s than ')'s.
        return 1
