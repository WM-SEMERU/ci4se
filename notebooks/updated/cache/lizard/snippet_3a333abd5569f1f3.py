def GetSource(self, row, col, table=None):
    if table is None:
        table = self.grid.current_table
    value = self.code_array((row, col, table))
    if value is None:
        return ''
    else:
        return value