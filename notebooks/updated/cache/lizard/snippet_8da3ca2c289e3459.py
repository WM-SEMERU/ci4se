def as_dict(self):
    if not self.cursor.rowcount:
        return {}
    self._rewind()
    if self.cursor.rowcount == 1:
        return dict(self.cursor.fetchone())
    else:
        raise ValueError('More than one row')