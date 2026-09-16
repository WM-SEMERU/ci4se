def warm_night_frequency(tasmin, thresh='22 degC', freq='YS'):
    r
    thresh = utils.convert_units_to(thresh, tasmin)
    events = (tasmin > thresh) * 1
    return events.resample(time=freq).sum(dim='time')