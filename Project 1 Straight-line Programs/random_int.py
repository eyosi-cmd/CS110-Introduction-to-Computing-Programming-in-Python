# random_integer.py: Takes two integers a and b from the command line and
# writes a random integer between a (inclusive) and b (exclusive).

import random
import stdio
import sys

# Get two integer a and b from a commandline
a = int(sys.argv[1])
b = int(sys.argv[2])

# writes a random integer between a (inclusive) and b (exclusive).
stdio.writeln(random.randrange(a, b))
