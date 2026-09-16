def getShocks(self):
    super(self.__class__, self).getShocks()
    newborns = self.t_age == 0
    self.TranShkNow[newborns] = self.TranShkAggNow * self.wRteNow
    self.PermShkNow[newborns] = self.PermShkAggNow
    self.getUpdaters()
    pLvlErrNew = self.getpLvlError()
    self.pLvlErrNow *= pLvlErrNew
    PermShkPcvd = self.PermShkNow / pLvlErrNew
    PermShkPcvd[self.update] *= self.pLvlErrNow[self.update]
    self.pLvlErrNow[self.update] = 1.0
    self.PermShkNow = PermShkPcvd