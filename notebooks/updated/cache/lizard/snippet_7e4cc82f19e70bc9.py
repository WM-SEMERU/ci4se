def from_characteristic_rate(cls, min_mag, b_val, char_mag, char_rate,
    bin_width):
    a_incr = b_val * (char_mag - 1.25) + numpy.log10(char_rate / DELTA_CHAR)
    a_val = a_incr - numpy.log10(b_val * numpy.log(10))
    return cls(min_mag, a_val, b_val, char_mag, char_rate, bin_width)