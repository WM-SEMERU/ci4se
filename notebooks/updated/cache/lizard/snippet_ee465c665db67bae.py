def sort(self, column_or_label, descending=False, distinct=False):
    column = self._get_column(column_or_label)
    if distinct:
        _, row_numbers = np.unique(column, return_index=True)
    else:
        row_numbers = np.argsort(column, axis=0, kind='mergesort')
    assert (row_numbers < self.num_rows).all(), row_numbers
    if descending:
        row_numbers = np.array(row_numbers[::-1])
    return self.take(row_numbers)