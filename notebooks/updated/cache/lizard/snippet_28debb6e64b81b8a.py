def sphere_ball_intersection(R, r):
    x = (2 * R ** 2 - r ** 2) / (2 * R)
    if x >= -R:
        return 2 * np.pi * R * (R - x)
    if x < -R:
        return 4 * np.pi * R ** 2