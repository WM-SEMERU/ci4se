def heating_degree_days(tas, thresh='17.0 degC', freq='YS'):
    r
    thresh = utils.convert_units_to(thresh, tas)
    return tas.pipe(lambda x: thresh - x).clip(0).resample(time=freq).sum(dim
        ='time')