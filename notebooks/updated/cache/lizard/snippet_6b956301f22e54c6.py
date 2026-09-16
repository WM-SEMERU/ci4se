def alter_change_column(self, table, column, field):
    return self._update_column(table, column, lambda a, b: b)