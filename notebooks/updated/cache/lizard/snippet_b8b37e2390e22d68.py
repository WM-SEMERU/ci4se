def set_temperature(self, temperature):
    velocities = np.random.randn(len(self.structure), 3)
    atomic_masses = np.array([site.specie.atomic_mass.to('kg') for site in
        self.structure])
    dof = 3 * len(self.structure) - 3
    velocities /= atomic_masses[:, (np.newaxis)] ** (1 / 2)
    velocities -= np.average(atomic_masses[:, (np.newaxis)] * velocities,
        axis=0) / np.average(atomic_masses)
    energy = np.sum(1 / 2 * atomic_masses * np.sum(velocities ** 2, axis=1))
    scale = (temperature * dof / (2 * energy / const.k)) ** (1 / 2)
    velocities *= scale * 1e-05
    self.temperature = temperature
    try:
        del self.structure.site_properties['selective_dynamics']
    except KeyError:
        pass
    try:
        del self.structure.site_properties['predictor_corrector']
    except KeyError:
        pass
    self.structure.add_site_property('velocities', velocities.tolist())