def compute(self, rtdc_ds):
    data = self.method(rtdc_ds)
    dsize = len(rtdc_ds) - len(data)
    if dsize > 0:
        msg = 'Growing feature {} in {} by {} to match event number!'
        warnings.warn(msg.format(self.feature_name, rtdc_ds, abs(dsize)),
            BadFeatureSizeWarning)
        data.resize(len(rtdc_ds), refcheck=False)
        data[-dsize:] = np.nan
    elif dsize < 0:
        msg = 'Shrinking feature {} in {} by {} to match event number!'
        warnings.warn(msg.format(self.feature_name, rtdc_ds, abs(dsize)),
            BadFeatureSizeWarning)
        data.resize(len(rtdc_ds), refcheck=False)
    if isinstance(data, np.ndarray):
        data.setflags(write=False)
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, np.ndarray):
                item.setflags(write=False)
    return data