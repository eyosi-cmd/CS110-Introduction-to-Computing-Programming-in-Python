"""
ring_buffer.py

Models a ring buffer.
"""

import stdarray
import stdio
import sys


def create(capacity):
    """
    Create and return a ring buffer, with the given maximum capacity and
    with all elements initialized to None. A ring buffer is represented as
    a list of four elements: the buffer (buff) itself as a list; number of
    elements (size) currently in buff; the index (first) of the least
    recently inserted item; and the index (last) one beyond the most recently
    inserted item.
    """

    # creating a four element as a list rb that is insialiazed.
    rb = stdarray.create1D(4, 0)
    # the first element create from capacity and return rb(ring buffer)
    rb[0] = stdarray.create1D(capacity)

    return rb


def capacity(rb):
    """
    Return the capacity of the ring buffer.
    """

    # return the length of rb(ring buffer) at the first index.
    return len(rb[0])


def size(rb):
    """
    Return the number of items currently in the buffer rb.
    """

    # return an the number of item at rb[1]
    return rb[1]


def is_empty(rb):
    """
    Return True if the buffer rb is empty and False otherwise.
    """
    # returns True if rb is empty, and False if not.
    if rb[1] == 0:
        return True

    else:
        return False


def is_full(rb):
    """
    Return True if the buffer rb is full and False otherwise.
    """

    # Return True if the size of ring buffer equal to capacity.
    # If not return False.
    if rb[1] == len(rb[0]):
        return True

    else:
        return False


def enqueue(rb, x):
    """
    Add item x to the end of the buffer rb.
    """

    # check if ring buffer is full.
    # if it is end the program.
    if is_full(rb):
        sys.exit('Error: cannot enqueue a full buffer')

    # because 4 elements are created
    # Use rb[3] to check the index as the end of buffer.
    rb[0][rb[3]] = x

    if rb[3] + 1 == len(rb[0]):
        rb[3] = 0

    else:
        rb[3] += 1

    rb[1] += 1


def dequeue(rb):
    """
    Delete and return item from the front of the buffer rb.
    """

    # make sure to check if rb is empty
    if is_empty(rb):
        sys.exit('Error: cannot dequeue an empty buffer')

    # set item, delete the value of the front of rb,
    # ruturn item after.
    item = rb[0][rb[2]]

    # else increment 1st idex by 1
    # decrement the 2nd idex by 1
    if rb[2] + 1 == len(rb[0]):
        rb[2] = 0

    else:
        rb[2] += 1

    rb[1] -= 1

    return item


def peek(rb):
    """
    Return (but do not delete) item from the front of the buffer rb.
    """

    # if rb is empity, exist
    if is_empty(rb):
        sys.exit('Error: cannot peek an empty buffer')

    # return rb with index rb[0][rb[2]]
    return rb[0][rb[2]]


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    rb = create(N)
    for i in range(1, N + 1):
        enqueue(rb, i)
    t = dequeue(rb)
    enqueue(rb, t)
    stdio.writef('Size after wrap-around is %d\n', size(rb))
    while size(rb) >= 2:
        x = dequeue(rb)
        y = dequeue(rb)
        enqueue(rb, x + y)
    stdio.writeln(peek(rb))


if __name__ == '__main__':
    _main()
