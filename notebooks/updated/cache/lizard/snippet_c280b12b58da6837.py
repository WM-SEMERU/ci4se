def fast_check_serializable(self, df):
    i_dtype, f_dtypes = df.index.dtype, df.dtypes
    index_has_object = df.index.dtype is NP_OBJECT_DTYPE
    fields_with_object = [f for f in df.columns if f_dtypes[f] is
        NP_OBJECT_DTYPE]
    if df.empty or not index_has_object and not fields_with_object:
        arr, _ = self._to_records(df.iloc[:10])
        return arr, {}
    df_objects_only = df[fields_with_object if fields_with_object else df.
        columns[:2]]
    arr, dtype = self._to_records(df_objects_only)
    return arr, {f: dtype[f] for f in dtype.names}