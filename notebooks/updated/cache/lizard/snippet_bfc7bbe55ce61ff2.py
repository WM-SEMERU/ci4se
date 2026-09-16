def remove_spin(self):
    for site in self.sites:
        new_sp = collections.defaultdict(float)
        for sp, occu in site.species.items():
            oxi_state = getattr(sp, 'oxi_state', None)
            new_sp[Specie(sp.symbol, oxidation_state=oxi_state)] += occu
        site.species = new_sp