def tx_days_above(tasmax, thresh='25.0 degC', freq='YS'):
    r
    thresh = utils.convert_units_to(thresh, tasmax)
    f = (tasmax > thresh) * 1
    return f.resample(time=freq).sum(dim='time')