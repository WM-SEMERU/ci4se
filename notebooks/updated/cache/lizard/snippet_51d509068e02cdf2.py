def read_single_knmi_file(filename):
    hourly_data_obs_raw = pd.read_csv(filename, parse_dates=[['YYYYMMDD',
        'HH']], date_parser=lambda yyyymmdd, hh: pd.datetime(int(str(
        yyyymmdd)[0:4]), int(str(yyyymmdd)[4:6]), int(str(yyyymmdd)[6:8]), 
        int(hh) - 1), skiprows=31, skipinitialspace=True, na_values='',
        keep_date_col=True)
    hourly_data_obs_raw.index = hourly_data_obs_raw['YYYYMMDD_HH']
    hourly_data_obs_raw.index = hourly_data_obs_raw.index + pd.Timedelta(hours
        =1)
    columns_hourly = ['temp', 'precip', 'glob', 'hum', 'wind', 'ssd']
    hourly_data_obs = pd.DataFrame(index=hourly_data_obs_raw.index, columns
        =columns_hourly, data=dict(temp=hourly_data_obs_raw['T'] / 10 + 
        273.15, precip=hourly_data_obs_raw['RH'] / 10, glob=
        hourly_data_obs_raw['Q'] * 10000 / 3600.0, hum=hourly_data_obs_raw[
        'U'], wind=hourly_data_obs_raw['FH'] / 10, ssd=hourly_data_obs_raw[
        'SQ'] * 6))
    negative_values = hourly_data_obs['precip'] < 0.0
    hourly_data_obs.loc[negative_values, 'precip'] = 0.0
    return hourly_data_obs