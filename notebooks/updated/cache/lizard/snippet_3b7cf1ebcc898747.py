def _unpack(self, data):
    current = self
    while current is not None:
        data = current._parser.unpack(data, current)
        last = current
        current = getattr(current, '_sub', None)
    _set(last, '_extra', data)