def tg_max(tas, freq='YS'):
    r
    return tas.resample(time=freq).max(dim='time', keep_attrs=True)