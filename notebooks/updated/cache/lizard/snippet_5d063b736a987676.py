def create_index(self, columns, name=None, **kw):
    columns = [normalize_column_name(c) for c in ensure_tuple(columns)]
    with self.db.lock:
        if not self.exists:
            raise DatasetException('Table has not been created yet.')
        for column in columns:
            if not self.has_column(column):
                return
        if not self.has_index(columns):
            self._threading_warn()
            name = name or index_name(self.name, columns)
            columns = [self.table.c[c] for c in columns]
            idx = Index(name, *columns, **kw)
            idx.create(self.db.executable)