def data_slice(self, slice_ind):
    if self.height is None:
        return self.data[slice_ind]
    return self.data[slice_ind, ...]