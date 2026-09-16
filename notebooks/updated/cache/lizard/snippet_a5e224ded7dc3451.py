def to_funset(self, discrete):
    fs = self.clampings.to_funset('exp')
    fs = fs.union(self.setup.to_funset())
    for i, row in self.readouts.iterrows():
        for var, val in row.iteritems():
            if not np.isnan(val):
                fs.add(gringo.Fun('obs', [i, var, discrete(val)]))
    return fs