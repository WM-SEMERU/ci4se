def dropna(self, dim, how='any', thresh=None):
    ds = self._to_temp_dataset().dropna(dim, how=how, thresh=thresh)
    return self._from_temp_dataset(ds)