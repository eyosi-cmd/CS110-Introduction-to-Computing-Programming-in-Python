import stdio
import sys


# Returns the domain type of the given URL.
def domain_type(URL):
    lk = URL.split('http://')
    lk = lk[1].split('/')
    lk = lk[0].split('.')
    domain = ''

    if(len(lk) > 2):
        for v in range(2, len(lk)):
            domain = domain + str(lk[v]) + '.'
        return domain[0:len(domain)-1]
    else:
        return domain[1]

# Test client [DO NOT EDIT]. Reads a URL as command-line argument and writes
# its domain type.


def _main():
    URL = sys.argv[1]
    stdio.writeln(domain_type(URL))


if __name__ == '__main__':
    _main()
