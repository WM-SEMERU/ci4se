def _arc(self, prom, sig):
    arcm = arc(prom['ra'], prom['decl'], sig['ra'], sig['decl'], self.mcRA,
        self.lat)
    arcz = arc(prom['raZ'], prom['declZ'], sig['raZ'], sig['declZ'], self.
        mcRA, self.lat)
    return {'arcm': arcm, 'arcz': arcz}