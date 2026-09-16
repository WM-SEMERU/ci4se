def _dEndfr(self):
    Mc = self._chirp_mass()
    return np.pi ** (2.0 / 3.0) * Mc ** (5.0 / 3.0) / (3.0 * (1.0 + self.z) **
        (1.0 / 3.0) * (self.freqs_orb / (1.0 + self.z)) ** (1.0 / 3.0)) * (
        2.0 / self.n) ** (2.0 / 3.0) * self._g_func() / self._f_func()