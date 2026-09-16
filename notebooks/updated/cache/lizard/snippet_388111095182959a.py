def setAndUpdateValues(self, solution_next, IncomeDstn, LivPrb, DiscFac):
    self.DiscFacEff = DiscFac * LivPrb
    self.ShkPrbsNext = IncomeDstn[0]
    self.PermShkValsNext = IncomeDstn[1]
    self.TranShkValsNext = IncomeDstn[2]
    self.PermShkMinNext = np.min(self.PermShkValsNext)
    self.TranShkMinNext = np.min(self.TranShkValsNext)
    self.vPfuncNext = solution_next.vPfunc
    self.WorstIncPrb = np.sum(self.ShkPrbsNext[self.PermShkValsNext * self.
        TranShkValsNext == self.PermShkMinNext * self.TranShkMinNext])
    if self.CubicBool:
        self.vPPfuncNext = solution_next.vPPfunc
    if self.vFuncBool:
        self.vFuncNext = solution_next.vFunc
    self.PatFac = (self.Rfree * self.DiscFacEff) ** (1.0 / self.CRRA
        ) / self.Rfree
    self.MPCminNow = 1.0 / (1.0 + self.PatFac / solution_next.MPCmin)
    self.ExIncNext = np.dot(self.ShkPrbsNext, self.TranShkValsNext * self.
        PermShkValsNext)
    self.hNrmNow = self.PermGroFac / self.Rfree * (self.ExIncNext +
        solution_next.hNrm)
    self.MPCmaxNow = 1.0 / (1.0 + self.WorstIncPrb ** (1.0 / self.CRRA) *
        self.PatFac / solution_next.MPCmax)