def add_filter(self, table, cols, condition):
    if table is not None and table not in self.relations:
        raise ItsdbError(
            'Cannot add filter; table "{}" is not defined by the relations file.'
            .format(table))
    if cols is None:
        cols = [None]
    self.filters[table].append((cols, condition))