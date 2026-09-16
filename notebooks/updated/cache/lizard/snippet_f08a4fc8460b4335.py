def cos_zen(utc_time, lon, lat):
    lon = np.deg2rad(lon)
    lat = np.deg2rad(lat)
    r_a, dec = sun_ra_dec(utc_time)
    h__ = _local_hour_angle(utc_time, lon, r_a)
    return np.sin(lat) * np.sin(dec) + np.cos(lat) * np.cos(dec) * np.cos(h__)