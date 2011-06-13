#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=2
# Print the sum of the even numbers in the Fibonacci sequence, up to 4 million


def fibo(lim):
    """
    yield the Fibonacci sequence
    """
    a, b = 0, 1
    while a < lim:
        yield a
        a, b = b, a + b


print sum([n for n in fibo(4000000) if n % 2])