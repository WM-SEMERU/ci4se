def bandpass(ts, low_hz, high_hz, order=3):
    orig_ndim = ts.ndim
    if ts.ndim is 1:
        ts = ts[:, (np.newaxis)]
    channels = ts.shape[1]
    fs = (len(ts) - 1.0) / (ts.tspan[-1] - ts.tspan[0])
    nyq = 0.5 * fs
    low = low_hz / nyq
    high = high_hz / nyq
    b, a = signal.butter(order, [low, high], btype='band')
    if not np.all(np.abs(np.roots(a)) < 1.0):
        raise ValueError('Filter will not be stable with these values.')
    dtype = ts.dtype
    output = np.zeros((len(ts), channels), dtype)
    for i in range(channels):
        output[:, (i)] = signal.filtfilt(b, a, ts[:, (i)])
    if orig_ndim is 1:
        output = output[:, (0)]
    return Timeseries(output, ts.tspan, labels=ts.labels)