def meter_data_from_csv(filepath_or_buffer, tz=None, start_col='start',
    value_col='value', gzipped=False, freq=None, **kwargs):
    read_csv_kwargs = {'usecols': [start_col, value_col], 'dtype': {
        value_col: np.float64}, 'parse_dates': [start_col], 'index_col':
        start_col}
    if gzipped:
        read_csv_kwargs.update({'compression': 'gzip'})
    read_csv_kwargs.update(kwargs)
    df = pd.read_csv(filepath_or_buffer, **read_csv_kwargs).tz_localize('UTC')
    if tz is not None:
        df = df.tz_convert(tz)
    if freq == 'hourly':
        df = df.resample('H').sum()
    elif freq == 'daily':
        df = df.resample('D').sum()
    return df