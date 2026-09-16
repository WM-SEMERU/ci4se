def derivativeZ(self, mLvl, pLvl, MedShk):
    xLvl = self.xFunc(mLvl, pLvl, MedShk)
    dxdShk = self.xFunc.derivativeZ(mLvl, pLvl, MedShk)
    dcdx = self.cFunc.derivativeX(xLvl, MedShk)
    dcdShk = dxdShk * dcdx + self.cFunc.derivativeY(xLvl, MedShk)
    dMeddShk = (dxdShk - dcdShk) / self.MedPrice
    return dcdShk, dMeddShk