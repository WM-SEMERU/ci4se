def maybe_set_size(self, min_itemsize=None):
    if _ensure_decoded(self.kind) == 'string':
        if isinstance(min_itemsize, dict):
            min_itemsize = min_itemsize.get(self.name)
        if min_itemsize is not None and self.typ.itemsize < min_itemsize:
            self.typ = _tables().StringCol(itemsize=min_itemsize, pos=self.pos)