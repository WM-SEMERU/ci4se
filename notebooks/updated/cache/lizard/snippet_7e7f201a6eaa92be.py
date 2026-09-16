def fit_cosine_function(wind):
    wind_daily = wind.groupby(wind.index.date).mean()
    wind_daily_hourly = pd.Series(index=wind.index, data=wind_daily.loc[
        wind.index.date].values)
    df = pd.DataFrame(data=dict(daily=wind_daily_hourly, hourly=wind)).dropna(
        how='any')
    x = np.array([df.daily, df.index.hour])
    popt, pcov = scipy.optimize.curve_fit(_cosine_function, x, df.hourly)
    return popt