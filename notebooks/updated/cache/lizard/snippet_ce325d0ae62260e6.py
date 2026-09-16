def q_vector(u, v, temperature, pressure, dx, dy, static_stability=1):
    r
    dudy, dudx = gradient(u, deltas=(dy, dx), axes=(-2, -1))
    dvdy, dvdx = gradient(v, deltas=(dy, dx), axes=(-2, -1))
    dtempdy, dtempdx = gradient(temperature, deltas=(dy, dx), axes=(-2, -1))
    q1 = -mpconsts.Rd / (pressure * static_stability) * (dudx * dtempdx + 
        dvdx * dtempdy)
    q2 = -mpconsts.Rd / (pressure * static_stability) * (dudy * dtempdx + 
        dvdy * dtempdy)
    return q1.to_base_units(), q2.to_base_units()