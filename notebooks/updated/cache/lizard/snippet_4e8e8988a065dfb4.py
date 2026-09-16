def PredictivePmf(self, xs, name=''):
    alpha0 = self.params.sum()
    ps = self.params / alpha0
    return MakePmfFromItems(zip(xs, ps), name=name)