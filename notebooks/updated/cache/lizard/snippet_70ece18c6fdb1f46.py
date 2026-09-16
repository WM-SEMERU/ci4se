def compute_degree_days(ts, heating_base_temperatures,
    cooling_base_temperatures):
    mean_sampling_rate = (ts.index[-1] - ts.index[0]).total_seconds() / (len
        (ts) - 1)
    if int(mean_sampling_rate / 86400.0) > 1:
        raise UnexpectedSamplingRate(
            'The sampling rate should be daily or shorter but found sampling rate: {}s'
            .format(mean_sampling_rate))
    ts_day = ts.resample(rule='D').mean()
    df = pd.DataFrame(calculate_temperature_equivalent(ts_day))
    for base in heating_base_temperatures:
        df = pd.concat([df, _calculate_degree_days(temperature_equivalent=
            df['temp_equivalent'], base_temperature=base)], axis=1)
    for base in cooling_base_temperatures:
        df = pd.concat([df, _calculate_degree_days(temperature_equivalent=
            df['temp_equivalent'], base_temperature=base, cooling=True)],
            axis=1)
    return df