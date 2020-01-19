# three_sort.py: Takes three integers as command-line arguments and prints
# them in ascending order, separated by spaces.

import stdio
import sys
import statistics

# Three int variables as a commandline argument.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
# Calculate a, b ,and c to put in assending:
a = min(min(x, y), min(y, z))
b = max(max(x, y), max(y, z))
# Find midpoint using midpoint formula.
mid = x + y + z - (a + b)
# print out by assending_order:
stdio.writeln(str(a)+" "+str(mid) + " " + str(b))
