def apply_operation(self, symmop, fractional=False):
    if not fractional:
        self._lattice = Lattice([symmop.apply_rotation_only(row) for row in
            self._lattice.matrix])

        def operate_site(site):
            new_cart = symmop.operate(site.coords)
            new_frac = self._lattice.get_fractional_coords(new_cart)
            return PeriodicSite(site.species, new_frac, self._lattice,
                properties=site.properties)
    else:
        new_latt = np.dot(symmop.rotation_matrix, self._lattice.matrix)
        self._lattice = Lattice(new_latt)

        def operate_site(site):
            return PeriodicSite(site.species, symmop.operate(site.
                frac_coords), self._lattice, properties=site.properties)
    self._sites = [operate_site(s) for s in self._sites]