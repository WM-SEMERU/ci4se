def validate_col(self, itemsize=None):
    if _ensure_decoded(self.kind) == 'string':
        c = self.col
        if c is not None:
            if itemsize is None:
                itemsize = self.itemsize
            if c.itemsize < itemsize:
                raise ValueError(
                    """Trying to store a string with len [{itemsize}] in [{cname}] column but
this column has a limit of [{c_itemsize}]!
Consider using min_itemsize to preset the sizes on these columns"""
                    .format(itemsize=itemsize, cname=self.cname, c_itemsize
                    =c.itemsize))
            return c.itemsize
    return None