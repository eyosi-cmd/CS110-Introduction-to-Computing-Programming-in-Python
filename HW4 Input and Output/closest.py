# closest.py: takes three floats x, y, and z from the command line, reads from
# standard input a sequence of coordinates (x_i, y_i, z_i), and writes the
# coordinates of the point closest to (x, y, z).

import stdio
import sys

# Read x, y, and z from command line, as floats.
x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

# Closest squared-distance so far, initialized to infinity.
bestD = float('inf')

# Read coordinates (xi, yi, zi) from standard input and calculate its
# squared-distance to the point (x, y, z). Check if that value is smaller
# than bestDist2, and if so, update bestDist2 to the new value, and
# let (bestx, besty, bestz) be (xi, yi, zi).
while stdio.isEmpty() is False:
    x1 = stdio.readFloat()
    y1 = stdio.readFloat()
    z1 = stdio.readFloat()
    if (((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2) < bestD):
        cx = x1
        cy = y1
        cz = z1
        bestD = ((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2)

# Write the closest point (bestx, besty, bestz).
stdio.writef('closest point = (%f, %f, %f)\n', cx, cy, cz)
