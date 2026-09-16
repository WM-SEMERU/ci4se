def _IndexedScan(self, i, max_records=None):
    self._ReadIndex()
    idx = 0
    start_ts = 0
    if i >= self._max_indexed:
        start_ts = max((0, 0), (self._index[self._max_indexed][0], self.
            _index[self._max_indexed][1] - 1))
        idx = self._max_indexed
    else:
        try:
            possible_idx = i - i % self.INDEX_SPACING
            start_ts = max(0, self._index[possible_idx][0]), self._index[
                possible_idx][1] - 1
            idx = possible_idx
        except KeyError:
            pass
    if max_records is not None:
        max_records += i - idx
    with data_store.DB.GetMutationPool() as mutation_pool:
        for ts, value in self.Scan(after_timestamp=start_ts, max_records=
            max_records, include_suffix=True):
            self._MaybeWriteIndex(idx, ts, mutation_pool)
            if idx >= i:
                yield idx, ts, value
            idx += 1