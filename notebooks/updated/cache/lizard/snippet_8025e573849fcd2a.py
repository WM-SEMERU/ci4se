def tiltFactor(xy, f, tilt, rot, center=None):
    x, y = xy
    arr = np.cos(tilt) * (1 + np.tan(tilt) / f * (x * np.sin(rot) - y * np.
        cos(rot))) ** 3
    return arr