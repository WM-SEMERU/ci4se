def from_tuples(cls, tuples, sortorder=None, names=None):
    if not is_list_like(tuples):
        raise TypeError('Input must be a list / sequence of tuple-likes.')
    elif is_iterator(tuples):
        tuples = list(tuples)
    if len(tuples) == 0:
        if names is None:
            msg = 'Cannot infer number of levels from empty list'
            raise TypeError(msg)
        arrays = [[]] * len(names)
    elif isinstance(tuples, (np.ndarray, Index)):
        if isinstance(tuples, Index):
            tuples = tuples._values
        arrays = list(lib.tuples_to_object_array(tuples).T)
    elif isinstance(tuples, list):
        arrays = list(lib.to_object_array_tuples(tuples).T)
    else:
        arrays = lzip(*tuples)
    return MultiIndex.from_arrays(arrays, sortorder=sortorder, names=names)