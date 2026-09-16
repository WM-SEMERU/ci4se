def to_polar(xyz):
    r = length_of(xyz)
    x, y, z = xyz
    theta = arcsin(z / r)
    phi = arctan2(y, x) % tau
    return r, theta, phi