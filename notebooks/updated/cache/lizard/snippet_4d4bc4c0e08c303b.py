def categorical_to_numeric(table):

    def transform(column):
        if is_categorical_dtype(column.dtype):
            return column.cat.codes
        if column.dtype.char == 'O':
            try:
                nc = column.astype(numpy.int64)
            except ValueError:
                classes = column.dropna().unique()
                classes.sort(kind='mergesort')
                nc = column.replace(classes, numpy.arange(classes.shape[0]))
            return nc
        elif column.dtype == bool:
            return column.astype(numpy.int64)
        return column
    if isinstance(table, pandas.Series):
        return pandas.Series(transform(table), name=table.name, index=table
            .index)
    elif _pandas_version_under0p23:
        return table.apply(transform, axis=0, reduce=False)
    else:
        return table.apply(transform, axis=0, result_type='reduce')