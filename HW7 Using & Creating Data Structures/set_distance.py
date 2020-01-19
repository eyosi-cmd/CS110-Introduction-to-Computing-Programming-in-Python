import stdio
import sys


# Returns the Jaccard index of the sets A and B.
def jaccard_index(A, B):

    return len(A.intersection(B)) / len(A.union(B))


# Returns the Jaccard distance between the two sets A and B.
def jaccard_distance(A, B):
    return 1 - jaccard_index(A, B)


# Test client [DO NOT EDIT]. Reads two command-line arguments, each
# comma-separated and representing the elements of a set, and writes the
# Jaccard distance between the two.
def _main():
    A = set(sys.argv[1].replace(' ', '').split(','))
    B = set(sys.argv[2].replace(' ', '').split(','))
    stdio.writeln(jaccard_distance(A, B))


if __name__ == '__main__':
    _main()
