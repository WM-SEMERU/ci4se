def temperature_data_from_json(data, orient='list'):
    if orient == 'list':
        df = pd.DataFrame(data, columns=['dt', 'tempF'])
        series = df.tempF
        series.index = pd.DatetimeIndex(df.dt).tz_localize('UTC')
        return series
    else:
        raise ValueError('orientation not recognized.')