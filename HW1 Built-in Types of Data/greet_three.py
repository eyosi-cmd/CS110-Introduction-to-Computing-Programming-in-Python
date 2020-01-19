# greet_three.py: takes three strings name1, name2, and name3 as command-line
# arguments and writes the output "Hi name3, name2, and name1.".

import stdio
import sys


# Get name1 from command line.
name1 = sys.argv[1]

# Get name2 from command line.
name2 = sys.argv[2]

# Get name3 from command line.
name3 = sys.argv[3]

# Write the output "Hi name3, name2, and name1.".
stdio.write("Hi ")
stdio.write(str(name3) + ", ")
stdio.write(str(name2) + ", and ")
stdio.writeln(str(name1)+".")
