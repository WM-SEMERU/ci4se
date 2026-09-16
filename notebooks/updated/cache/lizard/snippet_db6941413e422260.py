def center_of_mass(self):
    center = np.zeros(3)
    total_weight = 0
    for site in self:
        wt = site.species.weight
        center += site.coords * wt
        total_weight += wt
    return center / total_weight