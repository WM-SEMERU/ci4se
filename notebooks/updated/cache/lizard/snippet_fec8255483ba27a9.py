def decode(self, ids, strip_extraneous=False):
    if strip_extraneous:
        ids = strip_ids(ids, list(range(self._num_reserved_ids or 0)))
    return ' '.join(self.decode_list(ids))