def set_site_energies(self, energies):
    self.site_energies = energies
    for site_label in energies:
        for site in self.sites:
            if site.label == site_label:
                site.energy = energies[site_label]