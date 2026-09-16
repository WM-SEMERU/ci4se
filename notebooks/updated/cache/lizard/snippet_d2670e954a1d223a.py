def set_cols_dtype(self, array):
    self._check_row_size(array)
    self._dtype = array
    return self