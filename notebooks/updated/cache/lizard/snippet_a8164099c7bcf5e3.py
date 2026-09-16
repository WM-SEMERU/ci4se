def _from_axis_angle(cls, axis, angle):
    mag_sq = np.dot(axis, axis)
    if mag_sq == 0.0:
        raise ZeroDivisionError('Provided rotation axis has no length')
    if abs(1.0 - mag_sq) > 1e-12:
        axis = axis / sqrt(mag_sq)
    theta = angle / 2.0
    r = cos(theta)
    i = axis * sin(theta)
    return cls(r, i[0], i[1], i[2])