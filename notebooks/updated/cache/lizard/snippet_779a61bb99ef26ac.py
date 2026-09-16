def high_low(data, channels=None, high=None, low=None, full_output=False):
    if channels is None:
        data_ch = data
    else:
        data_ch = data[:, (channels)]
        if data_ch.ndim == 1:
            data_ch = data_ch.reshape((-1, 1))
    if high is None:
        if hasattr(data_ch, 'range'):
            high = [(np.Inf if di is None else di[1]) for di in data_ch.range()
                ]
            high = np.array(high)
        else:
            high = np.Inf
    if low is None:
        if hasattr(data_ch, 'range'):
            low = [(-np.Inf if di is None else di[0]) for di in data_ch.range()
                ]
            low = np.array(low)
        else:
            low = -np.Inf
    mask = np.all((data_ch < high) & (data_ch > low), axis=1)
    gated_data = data[mask]
    if full_output:
        HighLowGateOutput = collections.namedtuple('HighLowGateOutput', [
            'gated_data', 'mask'])
        return HighLowGateOutput(gated_data=gated_data, mask=mask)
    else:
        return gated_data