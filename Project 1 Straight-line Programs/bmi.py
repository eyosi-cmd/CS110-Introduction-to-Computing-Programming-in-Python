# bmi.py: Takes two floats w (for weight) and h (for height) as command-line
# arguments and prints the body mass index (BMI), calculated as the ratio of
# the weight to the square of the height.

import stdio
import sys

# Get float w and h as the commandline.
w = float(sys.argv[1])
h = float(sys.argv[2])

# Calculte BMI  w/h**2
stdio.writeln(w/h**2)
