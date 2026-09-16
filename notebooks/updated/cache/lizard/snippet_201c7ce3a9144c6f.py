def _keplerian_to_keplerian_circular(cls, coord, center):
    a, e, i, Ω, ω, ν = coord
    ex = e * cos(ω)
    ey = e * sin(ω)
    u = ω + ν
    return np.array([a, ex, ey, i, Ω, u], dtype=float)