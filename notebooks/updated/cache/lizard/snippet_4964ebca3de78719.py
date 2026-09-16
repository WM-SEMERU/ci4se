def triangle_area(p0, p1, p2):
    if p2.ndim < 2:
        p2 = p2[(np.newaxis), :]
    area = 0.5 * np.abs(p0[0] * p1[1] - p0[0] * p2[:, (1)] + p1[0] * p2[:,
        (1)] - p1[0] * p0[1] + p2[:, (0)] * p0[1] - p2[:, (0)] * p1[1])
    return area