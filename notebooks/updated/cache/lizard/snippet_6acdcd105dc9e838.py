def resample(self, sampling_rate, inplace=False, kind='linear'):
    if not inplace:
        var = self.clone()
        var.resample(sampling_rate, True, kind)
        return var
    if sampling_rate == self.sampling_rate:
        return
    old_sr = self.sampling_rate
    n = len(self.index)
    self.index = self._build_entity_index(self.run_info, sampling_rate)
    x = np.arange(n)
    num = len(self.index)
    from scipy.interpolate import interp1d
    f = interp1d(x, self.values.values.ravel(), kind=kind)
    x_new = np.linspace(0, n - 1, num=num)
    self.values = pd.DataFrame(f(x_new))
    assert len(self.values) == len(self.index)
    self.sampling_rate = sampling_rate