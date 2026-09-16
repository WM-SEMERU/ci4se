def frac_coords(self, frac_coords):
    self._frac_coords = np.array(frac_coords)
    self._coords = self._lattice.get_cartesian_coords(self._frac_coords)