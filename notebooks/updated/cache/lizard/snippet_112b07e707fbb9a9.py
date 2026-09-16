def _words_to_int(self, words, expected_bits=None):
    if expected_bits is None:
        expected_bits = len(words) * self._spi.bits_per_word
    shifts = range(0, expected_bits, self._spi.bits_per_word)[::-1]
    mask = 2 ** expected_bits - 1
    return reduce(or_, (word << shift for word, shift in zip(words, shifts))
        ) & mask