def resize(self, shape, format=None):
    if not self._resizeable:
        raise RuntimeError('RenderBuffer is not resizeable')
    if not (isinstance(shape, tuple) and len(shape) in (2, 3)):
        raise ValueError('RenderBuffer shape must be a 2/3 element tuple')
    if format is None:
        format = self._format
    elif isinstance(format, int):
        pass
    elif isinstance(format, string_types):
        if format not in ('color', 'depth', 'stencil'):
            raise ValueError(
                'RenderBuffer format must be "color", "depth" or "stencil", not %r'
                 % format)
    else:
        raise ValueError('Invalid RenderBuffer format: %r' % format)
    self._shape = tuple(shape[:2])
    self._format = format
    if self._format is not None:
        self._glir.command('SIZE', self._id, self._shape, self._format)