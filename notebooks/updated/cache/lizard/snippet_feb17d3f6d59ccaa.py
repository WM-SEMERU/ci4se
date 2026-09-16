def select(self, key, where=None, start=None, stop=None, columns=None,
    iterator=False, chunksize=None, auto_close=False, **kwargs):
    group = self.get_node(key)
    if group is None:
        raise KeyError('No object named {key} in the file'.format(key=key))
    where = _ensure_term(where, scope_level=1)
    s = self._create_storer(group)
    s.infer_axes()

    def func(_start, _stop, _where):
        return s.read(start=_start, stop=_stop, where=_where, columns=columns)
    it = TableIterator(self, s, func, where=where, nrows=s.nrows, start=
        start, stop=stop, iterator=iterator, chunksize=chunksize,
        auto_close=auto_close)
    return it.get_result()