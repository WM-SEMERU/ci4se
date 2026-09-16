def background_cutout_ma(self):
    if self._background is None:
        return None
    else:
        return np.ma.masked_array(self._background[self._slice], mask=self.
            _total_mask)