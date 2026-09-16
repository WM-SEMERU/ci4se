def get_lattice_quanta(self, convert_to_muC_per_cm2=True, all_in_polar=True):
    lattices = [s.lattice for s in self.structures]
    volumes = np.array([s.lattice.volume for s in self.structures])
    L = len(self.structures)
    e_to_muC = -1.6021766e-13
    cm2_to_A2 = 1e+16
    units = 1.0 / np.array(volumes)
    units *= e_to_muC * cm2_to_A2
    if convert_to_muC_per_cm2 and not all_in_polar:
        for i in range(L):
            lattice = lattices[i]
            l, a = lattice.lengths_and_angles
            lattices[i] = Lattice.from_lengths_and_angles(np.array(l) *
                units.ravel()[i], a)
    elif convert_to_muC_per_cm2 and all_in_polar:
        for i in range(L):
            lattice = lattices[-1]
            l, a = lattice.lengths_and_angles
            lattices[i] = Lattice.from_lengths_and_angles(np.array(l) *
                units.ravel()[-1], a)
    quanta = np.array([np.array(l.lengths_and_angles[0]) for l in lattices])
    return quanta