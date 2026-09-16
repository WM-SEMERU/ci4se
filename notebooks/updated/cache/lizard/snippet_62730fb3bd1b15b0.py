def get_last_filled_cell(self, table=None):
    maxrow = 0
    maxcol = 0
    for row, col, tab in self.dict_grid:
        if table is None or tab == table:
            maxrow = max(row, maxrow)
            maxcol = max(col, maxcol)
    return maxrow, maxcol, table