def mag_roll(RAW_IMU, inclination, declination):
    m = mag_rotation(RAW_IMU, inclination, declination)
    r, p, y = m.to_euler()
    return degrees(r)