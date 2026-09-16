def _op(self, operation, other, *allowed):
    f = self._field
    if self._combining:
        return reduce(self._combining, (q._op(operation, other, *allowed) for
            q in f))
    if __debug__ and _complex_safety_check(f, {operation} | set(allowed)):
        raise NotImplementedError('{self!r} does not allow {op} comparison.'
            .format(self=self, op=operation))
    if other is not None:
        other = f.transformer.foreign(other, (f, self._document))
    return Filter({self._name: {operation: other}})