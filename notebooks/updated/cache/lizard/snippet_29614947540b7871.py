def trans_v(self, structure):
    nsites = structure.num_sites
    volume = structure.volume
    natoms = structure.composition.num_atoms
    weight = float(structure.composition.weight)
    mass_density = 1660.5 * nsites * weight / (natoms * volume)
    if self.g_vrh < 0:
        raise ValueError(
            'k_vrh or g_vrh is negative, sound velocity is undefined')
    return (1000000000.0 * self.g_vrh / mass_density) ** 0.5