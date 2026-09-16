def replace(self, i, species, coords=None, coords_are_cartesian=False,
    properties=None):
    if coords is None:
        frac_coords = self[i].frac_coords
    elif coords_are_cartesian:
        frac_coords = self._lattice.get_fractional_coords(coords)
    else:
        frac_coords = coords
    new_site = PeriodicSite(species, frac_coords, self._lattice, properties
        =properties)
    self._sites[i] = new_site