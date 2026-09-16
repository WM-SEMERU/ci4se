def debye_temperature(self, structure):
    v0 = structure.volume * 1e-30 / structure.num_sites
    vl, vt = self.long_v(structure), self.trans_v(structure)
    vm = 3 ** (1.0 / 3.0) * (1 / vl ** 3 + 2 / vt ** 3) ** (-1.0 / 3.0)
    td = 1.05457e-34 / 1.38065e-23 * vm * (6 * np.pi ** 2 / v0) ** (1.0 / 3.0)
    return td