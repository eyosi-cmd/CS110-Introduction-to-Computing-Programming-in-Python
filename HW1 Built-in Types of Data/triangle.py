# triangle.py: takes three integers as command-line arguments and writes
# True if each one of them is less than or equal to the sum of the other two
# and False otherwise.

import stdio
import sys


# Get x from command line, as an int.

x = int(sys.argv[1])
# Get y from command line, as an int.

y = int(sys.argv[2])
# Get z from command line, as an int.

z = int(sys.argv[3])
# Using a single statement, write True if each of x, y, and z is less than
# or equal to the sum of the other two, and False otherwise.

if (x + y) >= z and (x+z) >= y and (y+z) >= x:
    stdio.writeln(True)
else:
    stdio.writeln(False)
