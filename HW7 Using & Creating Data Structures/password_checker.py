import stdio
import sys


# Returns True if pwd is a valid password and False otherwise.


def is_valid(pwd):

    if len(pwd) < 8:
        return False

    if pwd.isalnum():
        return False

    if pwd.isupper():
        return False

    if pwd.islower():
        return False

    for k in pwd:
        if k.isdigit():
            return True

        if k.isupper() or k.islower():
            return True

        if not k.isalnum():
            return True

        else:
            return False


# Test client [DO NOT EDIT]. Reads a password string as command-line argument
# and writes True if it's valid and False otherwise.

def _main():
    pwd = sys.argv[1]
    stdio.writeln(is_valid(pwd))


if __name__ == '__main__':
    _main()
