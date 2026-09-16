def update(self):
    self.kSS = ((self.getPermGroFacAggLR() ** self.CRRA / self.DiscFac - (
        1.0 - self.DeprFac)) / self.CapShare) ** (1.0 / (self.CapShare - 1.0))
    self.KtoYSS = self.kSS ** (1.0 - self.CapShare)
    self.wRteSS = (1.0 - self.CapShare) * self.kSS ** self.CapShare
    self.RfreeSS = 1.0 + self.CapShare * self.kSS ** (self.CapShare - 1.0
        ) - self.DeprFac
    self.MSS = self.kSS * self.RfreeSS + self.wRteSS
    self.convertKtoY = lambda KtoY: KtoY ** (1.0 / (1.0 - self.CapShare))
    self.Rfunc = lambda k: 1.0 + self.CapShare * k ** (self.CapShare - 1.0
        ) - self.DeprFac
    self.wFunc = lambda k: (1.0 - self.CapShare) * k ** self.CapShare
    self.KtoLnow_init = self.kSS
    self.MaggNow_init = self.kSS
    self.AaggNow_init = self.kSS
    self.RfreeNow_init = self.Rfunc(self.kSS)
    self.wRteNow_init = self.wFunc(self.kSS)
    self.PermShkAggNow_init = 1.0
    self.TranShkAggNow_init = 1.0
    self.makeAggShkDstn()
    self.AFunc = AggregateSavingRule(self.intercept_prev, self.slope_prev)