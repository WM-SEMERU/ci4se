def lon180to360(lon):
    if np.any(lon > 180.0) or np.any(lon < -180.0):
        print('Warning: lon outside expected range')
        lon = lon360to180(lon)
    lon = (lon + 360.0) % 360.0
    return lon