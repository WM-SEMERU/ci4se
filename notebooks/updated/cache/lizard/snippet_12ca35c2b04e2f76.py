def is_periodic_image(self, other, tolerance=1e-08, check_lattice=True):
    if check_lattice and self.lattice != other.lattice:
        return False
    if self.species != other.species:
        return False
    frac_diff = pbc_diff(self.frac_coords, other.frac_coords)
    return np.allclose(frac_diff, [0, 0, 0], atol=tolerance)