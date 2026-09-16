def _row_heights2pys(self):
    for row, tab in self.code_array.dict_grid.row_heights:
        if row < self.code_array.shape[0] and tab < self.code_array.shape[2]:
            height = self.code_array.dict_grid.row_heights[row, tab]
            height_strings = map(repr, [row, tab, height])
            self.pys_file.write('\t'.join(height_strings) + '\n')