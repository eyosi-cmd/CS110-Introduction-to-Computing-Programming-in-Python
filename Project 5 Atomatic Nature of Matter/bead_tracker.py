import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():
    # intialize P, tau, and delta.
    P, tau = int(sys.argv[1]), float(sys.argv[2])
    delta = float(sys.argv[3])

    firstPic = BlobFinder(Picture(sys.argv[4]), tau)
    prevBeads = firstPic.getBeads(P)

    for v in sys.argv[5:]:

        # construct blobfinder, currBeads, and a list of beads
        blobfinder = BlobFinder(Picture(v), tau)
        currBeads = blobfinder.getBeads(P)
        for currBead in currBeads:
            # map distances
            a = map(lambda x:
                    currBead.distanceTo(x), prevBeads)
            # filter the list
            minDist = list(filter(lambda x: x <= delta, a))
            # if the list isn't empty, write the min distance
            if minDist:
                minDist = min(minDist)
                stdio.writef('%.4f\n', minDist)

        # instialize prevBeads wiht currBeads
        prevBeads = currBeads
        stdio.writeln()


if __name__ == '__main__':
    main()
