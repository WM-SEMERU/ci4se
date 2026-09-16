def _ior(self, other):
    if not isinstance(other, _basebag):
        other = self._from_iterable(other)
    for elem, other_count in other.counts():
        old_count = self.count(elem)
        new_count = max(other_count, old_count)
        self._set_count(elem, new_count)
    return self