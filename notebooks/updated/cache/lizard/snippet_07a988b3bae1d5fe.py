def angular_distance(ra1, dec1, ra2, dec2):
    lon1 = np.deg2rad(ra1)
    lat1 = np.deg2rad(dec1)
    lon2 = np.deg2rad(ra2)
    lat2 = np.deg2rad(dec2)
    sdlon = np.sin(lon2 - lon1)
    cdlon = np.cos(lon2 - lon1)
    slat1 = np.sin(lat1)
    slat2 = np.sin(lat2)
    clat1 = np.cos(lat1)
    clat2 = np.cos(lat2)
    num1 = clat2 * sdlon
    num2 = clat1 * slat2 - slat1 * clat2 * cdlon
    denominator = slat1 * slat2 + clat1 * clat2 * cdlon
    return np.rad2deg(np.arctan2(np.sqrt(num1 ** 2 + num2 ** 2), denominator))