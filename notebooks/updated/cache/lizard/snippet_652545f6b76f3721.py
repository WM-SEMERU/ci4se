def get_spatially_integrated_flux(self, energies):
    if not isinstance(energies, np.ndarray):
        energies = np.array(energies, ndmin=1)
    results = [(self.spatial_shape.get_total_spatial_integral(energies) *
        component.shape(energies)) for component in self.components.values()]
    if isinstance(energies, u.Quantity):
        differential_flux = sum(results)
    else:
        differential_flux = np.sum(results, 0)
    return differential_flux