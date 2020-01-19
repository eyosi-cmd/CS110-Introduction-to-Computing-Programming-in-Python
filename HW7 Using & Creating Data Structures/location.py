import math
import stdio
import sys


class Location:
    """
    Represents a location on Earth.
    """

    def __init__(self, lat, lon):
        """
        Constructs a new location given its latitude and longitude values.
        """

        self._lat, self._lon = lat, lon

    def distanceTo(self, other):
        """
        Returns the great-circle distance between self and other.
        """
        s_lat = math.radians(self._lat)
        o_lat = math.radians(other._lat)
        s_lon = math.radians(self._lon)
        o_lon = math.radians(other._lon)
        Gc = 111 * math.acos(math.sin(s_lat) * math.sin(o_lat) +
                             math.cos(s_lat) * math.cos(o_lat) *
                             math.cos(s_lon - o_lon))
        return math.degrees(Gc)

    def __str__(self):
        """
        Returns a string representation of self.
        """

        return '(' + str(self._lat) + ', ' + str(self._lon) + ')'


# Test client [DO NOT EDIT]. Reads floats lat1, lon1, lat2, lon2 from command
# representing two locations on Earth, constructs two Location objects from
# them, and writes them along with the great-circle distance between the two.
def _main():
    lat1, lon1, lat2, lon2 = map(float, sys.argv[1:])
    loc1 = Location(lat1, lon1)
    loc2 = Location(lat2, lon2)
    stdio.writeln('loc1 = ' + str(loc1))
    stdio.writeln('loc2 = ' + str(loc2))
    stdio.writeln('d(loc1, loc2) = ' + str(loc1.distanceTo(loc2)))


if __name__ == '__main__':
    _main()
