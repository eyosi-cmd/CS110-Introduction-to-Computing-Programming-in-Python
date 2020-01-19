# order_check.py: Takes three floats values x, y, and z as command-line
# arguments and prints True if the values are strictly ascending or
# descending (i.e., x<y<z or x>y>z), and False otherwise.

import stdio
import sys


# Get x on command-line.
x = float(sys.argv[1])
# Get y on command-line.
y = float(sys.argv[2])
# Get z on command-line.
z = float(sys.argv[3])
# prints True if the values are strictly ascending or decending order.
if (x < y < z) or (x > y > z):
    stdio.writeln(True)
else:
    stdio.writeln(False)
