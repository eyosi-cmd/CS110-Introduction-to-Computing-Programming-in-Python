import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    count = 0
    total = 0.0
    while not stdio.isEmpty():
        disp = stdio.readFloat()
        disp *= 0.175e-6
        disp *= disp
        total += disp
        count += 1

    # cal var and intialize t, ETA, RHO, r
    var = total
    var /= 2 * count
    t = 297
    ETA = 9.135e-4
    RHO = 0.5e-6
    r = 8.31457

    # caluclate number of avogadro
    k = 6 * math.pi * var * ETA * RHO / t
    NA = r / k

    # print out the value
    stdio.write('Boltzman = ')
    stdio.writef('%e\n', k)
    stdio.write('Avogadro = ')
    stdio.writef('%e\n', NA)


if __name__ == '__main__':
    main()
