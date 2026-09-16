def from_frequency(cls, freq):
    if 0 < freq <= 20000:
        return super(Tone, cls).__new__(cls, freq)
    raise ValueError('invalid frequency: %.2f' % freq)