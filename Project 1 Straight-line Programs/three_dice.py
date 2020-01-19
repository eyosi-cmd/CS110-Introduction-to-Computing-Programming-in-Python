# three_dice.py: writes the sum of three random integers between 1 and 6, such
# as you might get when rolling three dice.

import random
import stdio
# three Random integers between 1 and 6

x = int(random.randrange(1, 6))
y = int(random.randrange(1, 6))
z = int(random.randrange(1, 6))
# print out sum of three rolling dice.

stdio.writeln(sum([x, y, z]))
