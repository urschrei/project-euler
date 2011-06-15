#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=5
# What is the smallest positive number that is evenly divisible by nums 1 - 20?


# Maybe cheating slightly, but it's trivial to implement using Euclid's method
from fractions import gcd


def lcm(largest):
    """
    Use reduce() to perform successive LCM operations
    on the products of the previous result and the next item in the range.
    We can use reduce() because the chosen LCM algorithm is associative:
    http://en.wikipedia.org/wiki/Associativity
    http://en.wikipedia.org/wiki/Least_common_multiple#Lattice-theoretic
    """
    return reduce(lambda x, y: (x * y) / gcd(x, y), range(1, largest))


print lcm(20)
