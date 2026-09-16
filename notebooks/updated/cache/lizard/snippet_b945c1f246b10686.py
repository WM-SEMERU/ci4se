def make_formatter(self, width, padding, alignment, overflow=None):
    if overflow is None:
        overflow = self.overflow_default
    if overflow == 'clip':
        overflower = lambda x: [x.clip(width, self.table.cliptext)]
    elif overflow == 'wrap':
        overflower = lambda x: x.wrap(width)
    elif overflow == 'preformatted':
        overflower = lambda x: x.split('\n')
    else:
        raise RuntimeError('Unexpected overflow mode: %r' % overflow)
    align = self.get_aligner(alignment, width)
    pad = self.get_aligner('center', width + padding)
    return lambda value: [pad(align(x)) for x in overflower(value)]