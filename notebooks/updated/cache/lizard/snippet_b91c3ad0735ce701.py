def random_point_triangle(triangle, use_int_coords=True):
    xs, ys = triangle.exterior.coords.xy
    A, B, C = zip(xs[:-1], ys[:-1])
    r1, r2 = np.random.rand(), np.random.rand()
    rx, ry = (1 - sqrt(r1)) * np.asarray(A) + sqrt(r1) * (1 - r2) * np.asarray(
        B) + sqrt(r1) * r2 * np.asarray(C)
    if use_int_coords:
        rx, ry = round(rx), round(ry)
        return Point(int(rx), int(ry))
    return Point(rx, ry)