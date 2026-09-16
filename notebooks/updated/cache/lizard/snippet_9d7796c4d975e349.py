def agg(self, aggregations):
    check_type(aggregations, list)
    df = _drop_str_columns(self)
    if len(df._data) == 0:
        raise ValueError('No results')
    new_index = Index(np.array(aggregations, dtype=np.bytes_), np.dtype(np.
        bytes_))
    new_data = OrderedDict((column.name, _series_agg(column, aggregations,
        new_index)) for column in df._iter())
    return DataFrame(new_data, new_index)