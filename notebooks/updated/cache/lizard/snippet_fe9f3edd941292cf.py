def build_stereographic_projection(center):
    p = center.position.au
    u = p / length_of(p)
    c = u.mean(axis=1)
    c = c / length_of(c)
    x_c, y_c, z_c = c

    def project(position):
        p = position.position.au
        u = p / length_of(p)
        x, y, z = u
        t0 = 1 / sqrt(x_c ** 2 + y_c ** 2)
        t1 = x * x_c
        t2 = sqrt(-z_c ** 2 + 1)
        t3 = t0 * t2
        t4 = y * y_c
        t5 = 1 / (t1 * t3 + t3 * t4 + z * z_c + 1)
        t6 = t0 * z_c
        return t0 * t5 * (x * y_c - x_c * y), -t5 * (t1 * t6 - t2 * z + t4 * t6
            )
    return project