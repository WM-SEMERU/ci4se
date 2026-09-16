def getShocks(self):
    employed = self.eStateNow == 1.0
    N = int(np.sum(employed))
    newly_unemployed = drawBernoulli(N, p=self.UnempPrb, seed=self.RNG.
        randint(0, 2 ** 31 - 1))
    self.eStateNow[employed] = 1.0 - newly_unemployed