"""
guitar_string.py

Models a guitar string.
"""

import math
import random
import ring_buffer
import stdarray
import stdio
import sys

# Sampling rate.
SPS = 44100


def create(frequency):

    """
    Create and return a guitar string of the given frequency, using a sampling
    rate given by SPS. A guitar string is represented as a ring buffer of
    of capacity N (SPS divided by frequency, rounded up to the nearest
    integer), with all values initialized to 0.0.
    """

    # calculating N then rouned up.
    N = int(math.ceil(SPS / frequncy))

    # create a guitar string by using ring buffer.
    string = ring_buffer.create(N)

    # use for loop for enqeue N.
    for v in range(N):
        ring_buffer.enqueue(string, 0.0)

    # return string
    return string


def create_from_samples(init):

    """
    Create and return a guitar string whose size and initial values are given
    by the list init.
    """

    # create a sample ring buffer
    # use for loop and make it equal to init
    samp_rg = ring_buffer.create(len(init))
    for v in init:
        ring_buffer.enqueue(samp_rg, v)

    return samp_rg


def pluck(string):
    """
    Pluck the given guitar string by replacing the buffer with white noise.
    """

    # All elements in ring buffer replaced with random float.
    for v in range(ring_buffer.capacity(string)):
        v = random.uniform(-0.5, 0.5)
        ring_buffer.dequeue(string)
        ring_buffer.enqueue(string, v)


def tic(string):
    """
    Advance the simulation one time step on the given guitar string by applying
    the Karplus-Strong update.
    """

    # set x with removed value of the ring buffer.
    x = ring_buffer.dequeue(string)

    # set y without removing value of rg.
    y = ring_buffer.peek(string)

    # set z as with Karplus-Strong update.
    # invoke enqueue with string and z
    z = 0.996 * 0.5 * (x + y)
    ring_buffer.enqueue(string, z)


def sample(string):
    """
    Return the current sample from the given guitar string.
    """

    # return ring buffer
    return ring_buffer.peek(string)


def _main():
    """
    Test client [DO NOT EDIT].
    """

    N = int(sys.argv[1])
    samples = [.2, .4, .5, .3, -.2, .4, .3, .0, -.1, -.3]
    test_string = create_from_samples(samples)
    for t in range(N):
        stdio.writef('%6d %8.4f\n', t, sample(test_string))
        tic(test_string)


if __name__ == '__main__':
    _main()
