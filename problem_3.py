#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=3
# Print the largest factor of 600851475143

import math

def factor(inp):
    """
    return factors of inp
    """
    yield 1
    counter = 2
    # we only need to test primes <= square root of the input
    limit = math.sqrt(inp)
    while counter <= limit:
        if inp % counter == 0:
            # it's a factor
            yield counter
            # factor the result into the input
            inp = (inp / counter)
            limit = math.sqrt(inp)
        else:
            counter += 1
    if inp > 1:
        yield inp


print sorted([int(f) for f in factor(600851475143)])[-1]

# Is there a more efficient way to do this using e.g. Pollard's p-1 method?
# ref: http://goo.gl/Z3KcX