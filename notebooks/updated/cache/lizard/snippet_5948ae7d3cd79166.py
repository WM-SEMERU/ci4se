def numeric_columns(self, include_bool=True):
    columns = []
    for col, dtype in zip(self.columns, self.dtypes):
        if is_numeric_dtype(dtype) and (include_bool or not include_bool and
            dtype != np.bool_):
            columns.append(col)
    return columns