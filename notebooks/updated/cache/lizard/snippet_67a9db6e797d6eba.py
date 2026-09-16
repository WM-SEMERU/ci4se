def interpolate(self, year):
    df = self.pivot_table(index=IAMC_IDX, columns=['year'], values='value',
        aggfunc=np.sum)
    if year in df.columns:
        df = df[np.isnan(df[year])]
    fill_values = df.apply(fill_series, raw=False, axis=1, year=year)
    fill_values = fill_values.dropna().reset_index()
    fill_values = fill_values.rename(columns={(0): 'value'})
    fill_values['year'] = year
    self.data = self.data.append(fill_values, ignore_index=True)