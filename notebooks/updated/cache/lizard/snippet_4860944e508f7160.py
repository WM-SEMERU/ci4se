def get_all_longest_col_lengths(self):
    response = {}
    for col in self.col_list:
        response[col] = self._longest_val_in_column(col)
    return response