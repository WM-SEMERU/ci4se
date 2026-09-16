def mjd2date(mjd, precision=3):
    from astropy.time import Time
    dt = Time(mjd, format='mjd', scale='utc').to_datetime()
    fracsec = ('%.*f' % (precision, 1e-06 * dt.microsecond)).split('.')[1]
    return '%04d/%02d/%02d/%02d:%02d:%02d.%s' % (dt.year, dt.month, dt.day,
        dt.hour, dt.minute, dt.second, fracsec)