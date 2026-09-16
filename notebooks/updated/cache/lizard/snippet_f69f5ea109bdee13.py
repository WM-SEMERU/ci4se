def _clean_body_df(self, df):
    if self.suffix == '-drvd.txt':
        df = df.dropna(subset=('temperature', 'reported_relative_humidity',
            'u_wind', 'v_wind'), how='all').reset_index(drop=True)
        df.units = {'pressure': 'hPa', 'reported_height': 'meter',
            'calculated_height': 'meter', 'temperature': 'Kelvin',
            'temperature_gradient': 'Kelvin / kilometer',
            'potential_temperature': 'Kelvin',
            'potential_temperature_gradient': 'Kelvin / kilometer',
            'virtual_temperature': 'Kelvin',
            'virtual_potential_temperature': 'Kelvin', 'vapor_pressure':
            'Pascal', 'saturation_vapor_pressure': 'Pascal',
            'reported_relative_humidity': 'percent',
            'calculated_relative_humidity': 'percent', 'u_wind':
            'meter / second', 'u_wind_gradient':
            '(meter / second) / kilometer)', 'v_wind': 'meter / second',
            'v_wind_gradient': '(meter / second) / kilometer)',
            'refractive_index': 'unitless'}
    else:
        df['u_wind'], df['v_wind'] = get_wind_components(df['speed'], np.
            deg2rad(df['direction']))
        df['u_wind'] = np.round(df['u_wind'], 1)
        df['v_wind'] = np.round(df['v_wind'], 1)
        df = df.dropna(subset=('temperature', 'direction', 'speed',
            'dewpoint_depression', 'u_wind', 'v_wind'), how='all').reset_index(
            drop=True)
        df['dewpoint'] = df['temperature'] - df['dewpoint_depression']
        df.drop('dewpoint_depression', axis=1, inplace=True)
        df.units = {'etime': 'second', 'pressure': 'hPa', 'height': 'meter',
            'temperature': 'degC', 'dewpoint': 'degC', 'direction':
            'degrees', 'speed': 'meter / second', 'u_wind':
            'meter / second', 'v_wind': 'meter / second'}
    return df