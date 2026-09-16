def solarReturnJD(jd, lon, forward=True):
    sun = swe.sweObjectLon(const.SUN, jd)
    if forward:
        dist = angle.distance(sun, lon)
    else:
        dist = -angle.distance(lon, sun)
    while abs(dist) > MAX_ERROR:
        jd = jd + dist / 0.9833
        sun = swe.sweObjectLon(const.SUN, jd)
        dist = angle.closestdistance(sun, lon)
    return jd