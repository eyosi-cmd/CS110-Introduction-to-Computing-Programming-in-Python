class Blob:
    """
    Represents a blob.
    """

    def __init__(self):
        """
        Constructs an empty blob.
        """
        # constract the amount of Pixels
        # set x, y as center of mass
        self._P = 0
        self._x, self._y = 0.0, 0.0

    def add(self, i, j):
        """
        Adds pixel (i, j) to this blob.
        """

        # find center of mass
        self._x = ((self._x) * (self._P) + i) / (self._P + 1)
        self._y = ((self._y) * (self._P) + j) / (self._P + 1)
        self._P += 1

    def mass(self):
        """
        Returns the number of pixels added to this blob, ie, its mass.
        """

        return self._P

    def distanceTo(self, other):
        """
        Returns the Euclidean distance between the center of mass of this blob
        and the center of mass of other blob.
        """

        # set x1 - x2 and y1 - y2
        xDist = self._x - other._x
        yDist = self._y - other._y
        # return Euclidean Distance
        return (xDist * xDist + yDist * yDist) ** 0.5

    def __str__(self):
        """
        Returns a string representation of this blob.
        """

        return '%d (%.4f, %.4f)' % (self._P, self._x, self._y)
