def astype(self, dtype, copy=True, errors='raise', **kwargs):
    if is_dict_like(dtype):
        if self.ndim == 1:
            if len(dtype) > 1 or self.name not in dtype:
                raise KeyError(
                    'Only the Series name can be used for the key in Series dtype mappings.'
                    )
            new_type = dtype[self.name]
            return self.astype(new_type, copy, errors, **kwargs)
        elif self.ndim > 2:
            raise NotImplementedError(
                'astype() only accepts a dtype arg of type dict when invoked on Series and DataFrames. A single dtype must be specified when invoked on a Panel.'
                )
        for col_name in dtype.keys():
            if col_name not in self:
                raise KeyError(
                    'Only a column name can be used for the key in a dtype mappings argument.'
                    )
        results = []
        for col_name, col in self.iteritems():
            if col_name in dtype:
                results.append(col.astype(dtype=dtype[col_name], copy=copy,
                    errors=errors, **kwargs))
            else:
                results.append(results.append(col.copy() if copy else col))
    elif is_extension_array_dtype(dtype) and self.ndim > 1:
        results = (self.iloc[:, (i)].astype(dtype, copy=copy) for i in
            range(len(self.columns)))
    else:
        new_data = self._data.astype(dtype=dtype, copy=copy, errors=errors,
            **kwargs)
        return self._constructor(new_data).__finalize__(self)
    result = pd.concat(results, axis=1, copy=False)
    result.columns = self.columns
    return result