def get_by_cols(self, cols, direction=1):
    if direction == 1:
        iterator = range(self.num_rows)
    elif direction == -1:
        iterator = range(self.num_rows - 1, -1, -1)
    else:
        raise ValueError(
            'Direction can only be 1 (first) or -1 (last). Got: {0}'.format
            (direction))
    for i in iterator:
        row = self._table[i + 1]
        all_sat = True
        for key, val in cols.items():
            if row[key] != val:
                all_sat = False
                break
        if all_sat:
            return row.copy()
    return None