def get_alt_az(utc_time, lon, lat):
    lon = np.deg2rad(lon)
    lat = np.deg2rad(lat)
    ra_, dec = sun_ra_dec(utc_time)
    h__ = _local_hour_angle(utc_time, lon, ra_)
    return np.arcsin(np.sin(lat) * np.sin(dec) + np.cos(lat) * np.cos(dec) *
        np.cos(h__)), np.arctan2(-np.sin(h__), np.cos(lat) * np.tan(dec) - 
        np.sin(lat) * np.cos(h__))