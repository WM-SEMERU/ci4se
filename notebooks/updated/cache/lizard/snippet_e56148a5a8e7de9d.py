def extract_row(self, row):
    new_row = []
    for col in range(self.get_grid_width()):
        new_row.append(self.get_tile(row, col))
    return new_row