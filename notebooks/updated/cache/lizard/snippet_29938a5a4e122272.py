def calcRandW(self, aLvlNow, pLvlNow):
    AaggPrev = np.mean(np.array(aLvlNow)) / np.mean(pLvlNow)
    AggregateK = np.mean(np.array(aLvlNow))
    PermShkAggNow = self.PermShkAggHist[self.Shk_idx]
    TranShkAggNow = self.TranShkAggHist[self.Shk_idx]
    self.Shk_idx += 1
    AggregateL = np.mean(pLvlNow) * PermShkAggNow
    KtoLnow = AggregateK / AggregateL
    self.KtoYnow = KtoLnow ** (1.0 - self.CapShare)
    RfreeNow = self.Rfunc(KtoLnow / TranShkAggNow)
    wRteNow = self.wFunc(KtoLnow / TranShkAggNow)
    MaggNow = KtoLnow * RfreeNow + wRteNow * TranShkAggNow
    self.KtoLnow = KtoLnow
    AggVarsNow = CobbDouglasAggVars(MaggNow, AaggPrev, KtoLnow, RfreeNow,
        wRteNow, PermShkAggNow, TranShkAggNow)
    return AggVarsNow