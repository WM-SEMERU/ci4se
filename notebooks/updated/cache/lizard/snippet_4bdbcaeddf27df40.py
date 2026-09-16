def set_data(self, data_np, metadata=None, order=None, astype=None):
    if astype:
        data = data_np.astype(astype, copy=False)
    else:
        data = data_np
    self._data = data
    self._calc_order(order)
    if metadata:
        self.update_metadata(metadata)
    self._set_minmax()
    self.make_callback('modified')