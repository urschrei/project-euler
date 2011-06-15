#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=5
# What is the smallest positive number that is evenly divisible by nums 1 - 20?


# Maybe cheating slightly, but it's trivial to implement using Euclid's method
from fractions import gcd


def lcm(largest):
    """
    use reduce() to perform successive LCM operations
    on the products of the previous result and the next item in the range.
    We can use reduce() because the chosen LCM algorithm is associative:
    http://en.wikipedia.org/wiki/Associativity
    http://en.wikipedia.org/wiki/Least_common_multiple#Lattice-theoretic
    """
    return reduce(lambda x, y: (x * y) / gcd(x, y), xrange(1, largest))


print lcm(20)


# Without reduce(), which is uglier, but perhaps clearer
def lcm_nonfunc(lrg):
    """
    assign successive output from the LCM algorithm to product
    """
    # we need an initial value
    product = 1
    for i in xrange(1, lrg):
        product = (product * i) / gcd(product, i)
    return product


print lcm_nonfunc(20)
# There are duplicate successive values; room for improvement (factorisation?)
