def to_pandas(self):
    if not self.is_raw():
        raise ValueError('Cannot convert to pandas Index if not evaluated.')
    from pandas import Index as PandasIndex
    return PandasIndex(self.values, self.dtype, name=self.name)