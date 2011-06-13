#!/usr/bin/env python

# http://projecteuler.net/index.php?section=problems&id=1
# Print the sum of all multiples of 3 or 5 below 1000

print sum([x for x in xrange(0,1000) if x % 3 == 0 or x % 5 == 0])