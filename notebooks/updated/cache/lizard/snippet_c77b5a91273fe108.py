def samples_by_indices_nomapping(self, indices):
    if not self._random_access:
        raise TypeError(
            'samples_by_indices_nomapping method not supported as one or more of the underlying data sources does not support random access'
            )
    batch = self.source.samples_by_indices_nomapping(indices)
    return self.fn(*batch)