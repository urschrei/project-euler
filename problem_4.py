#!/usr/bin/env python
# http://projecteuler.net/index.php?section=problems&id=4
# Return largest palindromic number of products <= 999


def palindrome(largest):
    """
    return largest palindromic number
    """
    l = []
    # nested for loops are a bit ugly, can probably improve this a lot
    for i in xrange(largest,100,-1):
        for j in xrange(largest,100,-1):
            check = (i * j)
            # <3 the ::-1 idiom <3<3
            if str(check) == str(check)[::-1]:
                l.append(check)
    return sorted(l)[-1]


print palindrome(999)
