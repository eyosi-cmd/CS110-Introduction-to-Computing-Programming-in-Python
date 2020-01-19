# trig_functions.py: takes a float t (angle in degrees) as command-line
# argument and writes the value of sin(2t)+sin(3t).

import math
import stdio
import sys


# Get t from command line, as a float.
t = float(sys.argv[1])

# Convert t to radians.
t = math.radians(t)

# Write the value of sin(2t) + sin(3t).
stdio.writeln(math.sin(2*t) + math.sin(3*t))
