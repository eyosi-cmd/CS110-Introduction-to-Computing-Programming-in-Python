# mercator.py: Takes three floats Lambda0, Phi, and Lambda as command-line
# arguments and prints its projection, i.e., the x and y values separated
# by a space, calculated using x=Lambda-Lambda0 and
# y=ln((1+sin(Phi))/(1-sin(Phi)))/2.

import math
import stdio
import sys


# Get the three floats Lambda0, Phi, and Lambda on the command-line

Lambda0 = float(sys.argv[1])
Phi = math.radians(float(sys.argv[2]))
Lambda = float(sys.argv[3])
# Find the values of x and y by using the formula that has given:

x = str(Lambda - Lambda0)
y = str(math.log((1+math.sin(Phi))/(1-math.sin(Phi)))/2)
# Get the outputs using x and y:

stdio.writeln(x + ' ' + y)
