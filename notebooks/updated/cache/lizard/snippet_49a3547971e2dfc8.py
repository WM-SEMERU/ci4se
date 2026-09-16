def extract(self, pos, width):
    pos = operator.index(pos)
    width = operator.index(width)
    if width < 0:
        raise ValueError('width must not be negative')
    if pos < 0:
        raise ValueError('extracting out of range')
    return BinWord(width, self >> pos, trunc=True)