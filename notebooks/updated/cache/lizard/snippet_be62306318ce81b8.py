def to_sparse(self, fill_value=None, kind='block'):
    from pandas.core.sparse.api import SparseDataFrame
    return SparseDataFrame(self._series, index=self.index, columns=self.
        columns, default_kind=kind, default_fill_value=fill_value)