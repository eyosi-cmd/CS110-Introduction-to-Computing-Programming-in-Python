import luminance
import stdarray
import stdio
import sys
from blob import Blob
from picture import Picture


class BlobFinder:
    """
    A data type for identifying blobs in a picture.
    """

    def __init__(self, pic, tau):
        """
        Constructs a blob finder to find blobs in the picture pic, using
        a luminance threshold tau.
        """

        # set the blobs list
        self._blobs = []

        # Create a 2D array list with booleans
        List = stdarray.create2D(pic.width(), pic.height(), False)

        # Enumerate the pixels of pics
        for i in range(pic.width()):
            for j in range(pic.height()):
                blob = Blob()
                self._findBlob(pic, tau, i, j, List, blob)
                if blob.mass() > 0:
                    self._blobs.append(blob)

    def _findBlob(self, pic, tau, i, j, List, blob):
        """
        Identifies a blob using depth-first search. The parameters are
        the picture (pic), luminance threshold (tau), pixel column (i),
        pixel row (j), 2D boolean matrix (List), and the blob being
        identified (blob).
        """

        # cheack if pixel i and j
        # or less than tau.
        if i > pic.width() - 1 or j > pic.height() - 1:
        List[i][j] = True

        # Add pixels in blob
        blob.add(i, j)

        # call _findBlob() on N, E, W, S pixels
        self._findBlob(pic, tau, i, j - 1, List, blob)
        self._findBlob(pic, tau, i + 1, j, List, blob)
        self._findBlob(pic, tau, i - 1, j, List, blob)
        self._findBlob(pic, tau, i, j + 1, List, blob)

    def getBeads(self, P):
        """
        Returns a list of all beads with >= P pixels.
        """

        beads = []
        for v in self._blobs:
            if v.mass() >= P:
                beads.append(v)

        return beads


# Takes an integer P, a float tau, and the name of a JPEG file as
# command-line arguments; writes out all of the beads with at least P
# pixels; and then writes out all of the blobs (beads with at least 1 pixel).
def _main():
    # construct Blobs with pic and tau
    P, tau = int(sys.argv[1]), float(sys.argv[2])
    pic = Picture(sys.argv[3])
    Blobs = BlobFinder(pic, tau)
    stdio.writeln(str(len(Blobs.getBeads(P))) + ' Beads:')

    # write each blob with mass >= P
    for i in Blobs.getBeads(P):
        stdio.writeln(i)
    # write each blob with mass >= 1
    stdio.writeln(str(len(Blobs.getBeads(1))) + ' Blobs:')
    for i in Blobs.getBeads(1):
        stdio.writeln(i)


if __name__ == '__main__':
    _main()
