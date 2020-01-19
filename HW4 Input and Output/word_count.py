# word_count.py: reads text from standard input and writes to standard output
# the number of words in the text.

import stdio

# Define a variable count to store the word count, with initial value 0.
count = 0

# Read words from standard input and for each word read increment count by one.
while stdio.isEmpty() is False:
    stdio.readString()
    count += 1

# Write the word count.
stdio.writef('number of words = %d\n', count)
