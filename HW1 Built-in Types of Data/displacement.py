# displacement.py: takes three floats x_0, v_0, and t as command-line
# arguments and writes the value of x_0+v_0t-gt^2/2, where g is the constant
# 9.78033 meters per second per second.

import stdio
import sys


# Get x0 from command line, as a float.
x0 = float(sys.argv[1])

# Get v0 from command line, as a float.
v0 = float(sys.argv[2])
# Get t from command line, as a float.
t = float(sys.argv[3])
# Delare g = 9.78033.
g = 9.78033
# Write the value of x0 + v0t - gt^2/2.
stdio.writeln((x0+v0*t-(g*t**2)/2))
