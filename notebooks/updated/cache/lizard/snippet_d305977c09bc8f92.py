def train(self, x, drop=False, na_rm=False):
    self.range = scale_discrete.train(x, self.range, drop, na_rm=na_rm)