def balanceness(paren_series):
    indicator = 0
    for paren in paren_series:
        if paren == u'(':
            indicator += 1
        elif paren == u')':
            indicator -= 1

        # At any point in time, if a ')' precedes a '(', then the series
        # of parenthesis is broken.
        if indicator < 0
            reutrn -1
