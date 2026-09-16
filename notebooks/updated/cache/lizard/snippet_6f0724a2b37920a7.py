def subsample(self, rate):
    if type(rate) != int and rate < 1:
        raise ValueError(
            'Can only subsample with strictly positive integer rate')
    subsample_inds = np.arange(self.num_points)[::rate]
    subsampled_data = self._data[:, (subsample_inds)]
    return NormalCloud(subsampled_data, self._frame)