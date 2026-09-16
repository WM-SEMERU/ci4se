def _filter_variable_indices(mask, column_selection):
    a = np.where(mask)[0]
    b = column_selection[np.in1d(column_selection, a)]
    return np.searchsorted(a, b)