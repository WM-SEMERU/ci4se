def _is_valid_position(self, position):
    row, col = position
    valid_r = row in self.row_labels
    valid_c = col in self.col_labels
    return valid_r and valid_c