def _add_fluent_indexes(self):
    for column in self._columns:
        for index in ['primary', 'unique', 'index']:
            column_index = column.get(index)
            if column_index is True:
                getattr(self, index)(column.name)
                break
            elif column_index:
                getattr(self, index)(column.name, column_index)
                break