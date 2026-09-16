def equivalent_crust_cohesion(self):
    deprecation('Will be moved to a function')
    if len(self.layers) > 1:
        crust = self.layer(0)
        crust_phi_r = np.radians(crust.phi)
        equivalent_cohesion = (crust.cohesion + crust.k_0 * self.
            crust_effective_unit_weight * self.layer_depth(1) / 2 * np.tan(
            crust_phi_r))
        return equivalent_cohesion