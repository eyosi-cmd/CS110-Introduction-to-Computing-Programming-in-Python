# longest_stretch.py: writes the longest contiguous sequence of equal
# integer values, from the sequence of integers read from the
# command line.

import stdio
import sys

# Create a list a consisting of the integers from the command line.
a = []
for v in sys.argv[1:]:
    a += [int(v)]

# Identify the starting position ms and length ml of the longest contiguous
# sequence of integers (ie, the longest stretch) from a.
cs = 0  # current stretch start
cl = 1  # current stretch length
ms = 0  # longest stretch start
ml = 0  # longest stretch length
for i in range(1, len(a)):
    # If a[i] is different from a[i - 1], then we have the start of a new
    # stretch. In that case: if cl is greater than ml, set ms to cs and ml
    # to cl; then, unconditionally set cs to i and cl to 1. If a[i] is
    # the same as a[i - 1], increment cl by 1.
    if a[i] != a[i - 1]:
        if (cl > ml):
            ms = cs
            ml = cl
        cs = i
        cl = 1
    else:
        cl += 1
# Again, if cl is greater than ml, set ms to cs and ml to cl, and set
# cs to i and cl to 1.
if (cl > ml):
    ms = cs
    ml = cl
    cs = i
    cl = 1

# Write the longest stretch from a, separating each by a space, and with a
# newline at the end.
for i in range(ms, ms + ml):
    if(i == ms + ml - 1):
        stdio.writeln(str(a[i]))
    else:
        stdio.write(str(a[i]) + ' ')
