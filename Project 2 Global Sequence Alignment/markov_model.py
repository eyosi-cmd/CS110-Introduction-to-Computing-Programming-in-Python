"""
markov_model.py

A data type that represents a Markov model of order k from a given text string.
"""

import stdio
import stdrandom
import sys


class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Creates a Markov model of order k from given text. Assumes that text
        has length at least k.
        """
        # get variables st, k
        self._k = k
        self._st = {}
        circ_text = text + text[:k]
        for i in range(len(circ_text) - k):

            # Fill out kgram using for loop
            kgram = circ_text[i:i + self._k]
            # get next_char using self._k
            next_char = circ_text[i + self._k]

            # Create a Markov model.
            self._st.setdefault(kgram, {next_char: 0})
            self._st[kgram].setdefault(next_char, 0)
            self._st[kgram][next_char] += 1

    def order(self):
        """
        Returns order k of Markov model.
        """

        return self._k

    def kgram_freq(self, kgram):
        """
        Returns number of occurrences of kgram in text. Raises an error if
        kgram is not of length k.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        # Check if kgram is not in _st,run error
        if kgram not in self._st:
            return 0
        # return the sum of list in self._st
        return sum(list(self._st[kgram].values()))

    def char_freq(self, kgram, c):
        """
        Returns number of times character c follows kgram. Raises an error if
        kgram is not of length k.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        # look if kgram is in _st
        if kgram not in self._st:
            return 0
        # look if c is in _st
        if c not in self._st[kgram]:
            return 0
        # return freq of c with kgram, if they are in _st
        return self._st[kgram][c]

    def rand(self, kgram):
        """
        Returns a random character following kgram. Raises an error if kgram
        is not of length k or if kgram is unknown.
        """

        if self._k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' +
                             str(self._k))
        if kgram not in self._st:
            raise ValueError('Unknown kgram ' + kgram)
        # get a, b by list _st with key(), value
        a = list(self._st[kgram].keys())
        b = list(self._st[kgram].values())
        # return a with index of random b
        return a[stdrandom.discrete(b)]

    def gen(self, kgram, T):
        """
        Generates and returns a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k characters of the
        generated string is the argument kgram. Assumes that T is at least k.
        """
        # text initialize text to kgram
        text = kgram
        for i in range(T - self._k):
            # call to rand method and append to text
            text += self.rand(kgram)
            # update kgram
            kgram = text[-self._k:]

        return text

    def replace_unknown(self, corrupted):
        """
        Replaces unknown characters (~) in corrupted with most probable
        characters, and returns that string.
        """

        # list a in argmax fun
        # return the index of the max of a
        def argmax(a):
            return a.index(max(a))

        original = ''
        for x in range(len(corrupted)):
            if corrupted[x] == '~':
                # before/after kgram initialized
                kgram_before = corrupted[x - self._k:x]
                kgram_after = corrupted[x + 1:self._k + x + 1]
                probs = []
                # set all outcomes from _st
                a = list(self._st[kgram_before].keys())
                # loop over the possible outcomes
                for i in a:
                    # create context as a string
                    context = kgram_before + i + kgram_after
                    c = 1.0
                    # try all chances in kgram, char
                    for v in range(self._k + 1):
                        # initialize each kgram and char
                        kgram = context[v:v + self._k]
                        char = context[v + self._k]

                        # call char freq
                        if self.char_freq(kgram, char) == 0:
                            c = 0.0
                            break

                        else:
                            # update c
                            c *= (self.char_freq(kgram, char)
                                  / self.kgram_freq(kgram))
                    # append chances 'c'
                    probs.append(c)
                # call argmax in list a as index probs
                # add origial list a
                original += a[argmax(probs)]

            else:
                # or else add corrupted
                original += corrupted[x]
        return original


def _main():
    """
    Test client [DO NOT EDIT].
    """

    text, k = sys.argv[1], int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace("-", " "), char.replace("-", " ")))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char,
                         model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
