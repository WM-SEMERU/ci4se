def background_sum(self):
    if self._background is not None:
        if self._is_completely_masked:
            return np.nan * self._background_unit
        else:
            return np.sum(self._background_values)
    else:
        return None