def from_numpy(cls, np_obj, name, columns, index=None, index_key=None, **kwargs
    ):
    if not np:
        raise LoadError('numpy could not be imported')
    _assert_is_type('numpy object', np_obj, np.ndarray)
    index = index or range(np_obj.shape[0])
    columns = list(map(str, columns))
    index_key = index_key or cls._default_index_key
    if len(index) != np_obj.shape[0]:
        raise LoadError(
            'length of index must be equal to number of rows of array')
    elif len(columns) != np_obj.shape[1]:
        raise LoadError(
            'length of columns must be equal to number of columns of array')
    data = cls(name=name, **kwargs)
    data.values = [dict([(index_key, cls.serialize(idx))] + [(col, x) for 
        col, x in zip(columns, row)]) for idx, row in zip(index, np_obj.
        tolist())]
    return data