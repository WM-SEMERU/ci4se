def _row_heights2xls(self, worksheets):
    xls_max_rows, xls_max_tabs = self.xls_max_rows, self.xls_max_tabs
    dict_grid = self.code_array.dict_grid
    for row, tab in dict_grid.row_heights:
        if row < xls_max_rows and tab < xls_max_tabs:
            height_pixels = dict_grid.row_heights[row, tab]
            height_inches = height_pixels / float(get_dpi()[1])
            height_points = height_inches * 72.0
            worksheets[tab].row(row).height_mismatch = True
            worksheets[tab].row(row).height = int(height_points * 20.0)