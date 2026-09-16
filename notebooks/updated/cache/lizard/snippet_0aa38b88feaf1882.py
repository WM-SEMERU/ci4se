def select(self, cols, mode='list'):
    if isinstance(cols, stringtypes):
        cols = _split_cols(cols)
    if not cols:
        cols = [f.name for f in self.fields]
    return select_rows(cols, self, mode=mode)