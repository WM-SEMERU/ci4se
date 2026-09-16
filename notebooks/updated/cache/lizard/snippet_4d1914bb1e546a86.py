def _insert_from_ordered_sequence(self, seq):
    if len(seq) == 0:
        return
    mid, greater, lesser = self._bisect(seq)
    self.insert(mid)
    self._insert_from_ordered_sequence(greater)
    self._insert_from_ordered_sequence(lesser)