def add_dos(self, label, dos):
    energies = (dos.energies - dos.efermi if self.zero_at_efermi else dos.
        energies)
    densities = dos.get_smeared_densities(self.sigma
        ) if self.sigma else dos.densities
    efermi = dos.efermi
    self._doses[label] = {'energies': energies, 'densities': densities,
        'efermi': efermi}