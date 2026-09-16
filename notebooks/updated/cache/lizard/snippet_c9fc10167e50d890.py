def highpass(timeseries, frequency, filter_order=8, attenuation=0.1):
    if not isinstance(timeseries, TimeSeries):
        raise TypeError('Can only resample time series')
    if timeseries.kind is not 'real':
        raise TypeError('Time series must be real')
    lal_data = timeseries.lal()
    _highpass_func[timeseries.dtype](lal_data, frequency, 1 - attenuation,
        filter_order)
    return TimeSeries(lal_data.data.data, delta_t=lal_data.deltaT, dtype=
        timeseries.dtype, epoch=timeseries._epoch)