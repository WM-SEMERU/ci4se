def warm_day_frequency(tasmax, thresh='30 degC', freq='YS'):
    r
    thresh = utils.convert_units_to(thresh, tasmax)
    events = (tasmax > thresh) * 1
    return events.resample(time=freq).sum(dim='time')