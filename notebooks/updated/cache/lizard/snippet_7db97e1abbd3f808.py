def fold_point(p, lattice, coords_are_cartesian=False):
    if coords_are_cartesian:
        p = lattice.get_fractional_coords(p)
    else:
        p = np.array(p)
    p = np.mod(p + 0.5 - 1e-10, 1) - 0.5 + 1e-10
    p = lattice.get_cartesian_coords(p)
    closest_lattice_point = None
    smallest_distance = 10000
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                lattice_point = np.dot((i, j, k), lattice.matrix)
                dist = np.linalg.norm(p - lattice_point)
                if closest_lattice_point is None or dist < smallest_distance:
                    closest_lattice_point = lattice_point
                    smallest_distance = dist
    if not np.allclose(closest_lattice_point, (0, 0, 0)):
        p = p - closest_lattice_point
    return p