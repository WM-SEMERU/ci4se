def indexables(self):
    if self._indexables is None:
        self._indexables = []
        self._indexables.extend([IndexCol(name=name, axis=axis, pos=i) for 
            i, (axis, name) in enumerate(self.attrs.index_cols)])
        dc = set(self.data_columns)
        base_pos = len(self._indexables)

        def f(i, c):
            klass = DataCol
            if c in dc:
                klass = DataIndexableCol
            return klass.create_for_block(i=i, name=c, pos=base_pos + i,
                version=self.version)
        self._indexables.extend([f(i, c) for i, c in enumerate(self.attrs.
            values_cols)])
    return self._indexables