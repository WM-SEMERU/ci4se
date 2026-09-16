def _getue(self):
    try:
        value, newpos = self._readue(0)
        if value is None or newpos != self.len:
            raise ReadError
    except ReadError:
        raise InterpretError(
            'Bitstring is not a single exponential-Golomb code.')
    return value