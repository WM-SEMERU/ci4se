def histogram2d(self, distance_modulus=None, delta_mag=0.03, steps=10000):
    if distance_modulus is not None:
        self.distance_modulus = distance_modulus
    mass_init, mass_pdf, mass_act, mag_1, mag_2 = self.sample(mass_steps=steps)
    bins_mag_1 = np.arange(self.mod + mag_1.min() - 0.5 * delta_mag, self.
        mod + mag_1.max() + 0.5 * delta_mag, delta_mag).astype(np.float32)
    bins_mag_2 = np.arange(self.mod + mag_2.min() - 0.5 * delta_mag, self.
        mod + mag_2.max() + 0.5 * delta_mag, delta_mag).astype(np.float32)
    isochrone_pdf = np.histogram2d(self.mod + mag_1, self.mod + mag_2, bins
        =[bins_mag_1, bins_mag_2], weights=mass_pdf)[0].astype(np.float32)
    return isochrone_pdf, bins_mag_1, bins_mag_2