def are_symmetrically_equivalent(self, sites1, sites2, symm_prec=0.001):

    def in_sites(site):
        for test_site in sites1:
            if test_site.is_periodic_image(site, symm_prec, False):
                return True
        return False
    for op in self:
        newsites2 = [PeriodicSite(site.species, op.operate(site.frac_coords
            ), site.lattice) for site in sites2]
        for site in newsites2:
            if not in_sites(site):
                break
        else:
            return True
    return False