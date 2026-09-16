def generate_orbital_path(self, factor=3.0, n_points=20, viewup=None,
    z_shift=None):
    if viewup is None:
        viewup = rcParams['camera']['viewup']
    center = list(self.center)
    bnds = list(self.bounds)
    if z_shift is None:
        z_shift = (bnds[5] - bnds[4]) * factor
    center[2] = center[2] + z_shift
    radius = (bnds[1] - bnds[0]) * factor
    y = (bnds[3] - bnds[2]) * factor
    if y > radius:
        radius = y
    return vtki.Polygon(center=center, radius=radius, normal=viewup,
        n_sides=n_points)