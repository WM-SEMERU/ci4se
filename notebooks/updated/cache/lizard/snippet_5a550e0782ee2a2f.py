def append_column(self, label, values):
    if not isinstance(label, str):
        raise ValueError(
            'The column label must be a string, but a {} was given'.format(
            label.__class__.__name__))
    if not isinstance(values, np.ndarray):
        if not _is_non_string_iterable(values):
            values = [values] * max(self.num_rows, 1)
        values = np.array(tuple(values))
    if self.num_rows != 0 and len(values) != self.num_rows:
        raise ValueError(
            'Column length mismatch. New column does not have the same number of rows as table.'
            )
    else:
        self._num_rows = len(values)
    self._columns[label] = values