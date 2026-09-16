def get_centered_molecule(self):
    center = self.center_of_mass
    new_coords = np.array(self.cart_coords) - center
    return self.__class__(self.species_and_occu, new_coords, charge=self.
        _charge, spin_multiplicity=self._spin_multiplicity, site_properties
        =self.site_properties)