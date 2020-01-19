# min_max.py: reads in floats (as many as the user enters) from standard
# input and writes out the minimum and maximum values along with their ranks,
# ie, their positions (starting at 1) in the input.

import stdio

# Smallest and largest floats.
neg_inf = float('-inf')
pos_inf = float('inf')

# Read floats from standard input an into list a
a = stdio.readAllFloats()

# define variales to keep track of min and max values and rank.
min_val, min_rank = pos_inf, 0
max_val, max_rank = neg_inf, 0

# Iterate the list a to identify the minimum value and its rank and the
# maximum value and its rank. If v is smaller than min_val, update min_val
# to v and min_rank to i + 1; similarly, update max_val and max_rank.
for i, v in enumerate(a):
    if (v < min_val):
        min_val = v
        min_rank = i + 1
    if (v > max_val):
        max_val = v
        max_rank = i + 1

# Write the results (min_val, min_rank, max_val, max_rank).
stdio.writef('min val = %f, min rank = %d\n', min_val, min_rank)
stdio.writef('max val = %f, max rank = %d\n', max_val, max_rank)
