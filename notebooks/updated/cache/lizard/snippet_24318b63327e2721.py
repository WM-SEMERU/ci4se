def parang(hourangle, declination, latitude):
    return -np.arctan2(-np.sin(hourangle), np.cos(declination) * np.tan(
        latitude) - np.sin(declination) * np.cos(hourangle))