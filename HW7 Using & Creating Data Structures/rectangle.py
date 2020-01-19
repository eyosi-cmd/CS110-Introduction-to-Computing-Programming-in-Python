import stdio
import sys
from interval import Interval


class Rectangle:
    """
    Represents a rectangle as two (x and y) intervals.
    """

    def __init__(self, xint, yint):
        """
        Constructs a new rectangle given the x and y intervals.
        """

        self._xint, self._yint = xint, yint

    def area(self):
        """
        Returns the area of self.
        """

        x = self._xint.rbound() - self._xint.lbound()
        y = self._yint.rbound() - self._yint.lbound()
        return x * y

    def perimeter(self):
        """
        Returns the perimeter of self.
        """
        x = self._xint.rbound() - self._xint.lbound()
        y = self._yint.rbound() - self._yint.lbound()
        return 2 * x + 2 * y

    def contains(self, x, y):
        """
        Returns True if self contains the point (x, y) and False otherwise.
        """

        if self._xint.contains(x):
            if self._yint.contains(y):
                return True

        return False

    def intersects(self, other):
        """
        Returns True if self intersects other and False othewise.
        """

        if self._xint.intersects(other._xint):
            if self._yint.intersects(other._yint):
                return True
        return False

    def __str__(self):
        """
        Returns a string representation of self.
        """

        return str(self._xint) + ' x ' + str(self._yint)


# Test client [DO NOT EDIT]. Reads a floats x and y from the command line and
# writes to standard output: all of the rectangles from standard input
# (each defined by two pairs of floats) that contain (x, y); and all pairs
# of rectangles from standard input that intersect one another.
def _main():
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    rectangles = []
    while not stdio.isEmpty():
        lbound1 = stdio.readFloat()
        rbound1 = stdio.readFloat()
        lbound2 = stdio.readFloat()
        rbound2 = stdio.readFloat()
        rectangles += [Rectangle(Interval(lbound1, rbound1),
                                 Interval(lbound2, rbound2))]
    for i in range(len(rectangles)):
        stdio.writef('Area(%s) = %f\n', rectangles[i], rectangles[i].area())
        stdio.writef('Perimeter(%s) = %f\n', rectangles[i],
                     rectangles[i].perimeter())
        if rectangles[i].contains(x, y):
            stdio.writef('%s contains (%f, %f)\n', rectangles[i], x, y)
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            if rectangles[i].intersects(rectangles[j]):
                stdio.writef('%s intersects %s\n',
                             rectangles[i], rectangles[j])


if __name__ == '__main__':
    _main()
