def declination_cooper69(dayofyear):
    day_angle = _calculate_simple_day_angle(dayofyear)
    dec = np.deg2rad(23.45 * np.sin(day_angle + 2.0 * np.pi / 365.0 * 285.0))
    return dec