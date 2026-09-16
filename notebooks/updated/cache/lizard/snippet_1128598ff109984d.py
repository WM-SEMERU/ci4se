def spa_python(time, latitude, longitude, altitude=0, pressure=101325,
    temperature=12, delta_t=67.0, atmos_refract=None, how='numpy',
    numthreads=4, **kwargs):
    lat = latitude
    lon = longitude
    elev = altitude
    pressure = pressure / 100
    atmos_refract = atmos_refract or 0.5667
    if not isinstance(time, pd.DatetimeIndex):
        try:
            time = pd.DatetimeIndex(time)
        except (TypeError, ValueError):
            time = pd.DatetimeIndex([time])
    unixtime = np.array(time.astype(np.int64) / 10 ** 9)
    spa = _spa_python_import(how)
    delta_t = delta_t or spa.calculate_deltat(time.year, time.month)
    app_zenith, zenith, app_elevation, elevation, azimuth, eot = (spa.
        solar_position(unixtime, lat, lon, elev, pressure, temperature,
        delta_t, atmos_refract, numthreads))
    result = pd.DataFrame({'apparent_zenith': app_zenith, 'zenith': zenith,
        'apparent_elevation': app_elevation, 'elevation': elevation,
        'azimuth': azimuth, 'equation_of_time': eot}, index=time)
    return result