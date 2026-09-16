def comparable(self):
    string_parts = []
    string_parts.append('table name: {0:s}'.format(self.table_name))
    string_parts.append('column name: {0:s}'.format(self.column_name))
    if self.row_condition is not None:
        row_condition_string = ' '.join(['{0!s}'.format(value) for value in
            self.row_condition])
        string_parts.append('row condition: "{0:s}"'.format(
            row_condition_string))
    if self.row_index is not None:
        string_parts.append('row index: {0:d}'.format(self.row_index))
    return self._GetComparable(sub_comparable_string=', '.join(string_parts))