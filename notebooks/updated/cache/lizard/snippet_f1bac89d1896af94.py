def _get_datatable_options(self):
    if not hasattr(self, '_datatable_options'):
        self._datatable_options = self.get_datatable_options()
        columns = self._datatable_options.get('columns', [])
        for i, column in enumerate(columns):
            if len(column) >= 2 and isinstance(column[1], list):
                column = list(column)
                column[1] = tuple(column[1])
                columns[i] = tuple(column)
    return self._datatable_options