def _maybe_to_sparse(array):
    if isinstance(array, ABCSparseSeries):
        array = array.values.copy()
    return array