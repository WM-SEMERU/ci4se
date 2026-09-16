def column_names(self):
    return [name for name, d in self._columns.items() if d.get('show', True)]