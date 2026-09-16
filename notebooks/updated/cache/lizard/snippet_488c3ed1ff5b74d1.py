def colRowIsOnSciencePixelList(self, col, row, padding=DEFAULT_PADDING):
    out = np.ones(len(col), dtype=bool)
    col_arr = np.array(col)
    row_arr = np.array(row)
    mask = np.bitwise_or(col_arr < 12.0 - padding, col_arr > 1111 + padding)
    out[mask] = False
    mask = np.bitwise_or(row_arr < 20.0 - padding, row_arr > 1043 + padding)
    out[mask] = False
    return out