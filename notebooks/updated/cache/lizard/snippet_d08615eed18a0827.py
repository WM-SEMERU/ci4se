def get_paged_slice(self, column_family, range, start_column, consistency_level
    ):
    self._seqid += 1
    d = self._reqs[self._seqid] = defer.Deferred()
    self.send_get_paged_slice(column_family, range, start_column,
        consistency_level)
    return d