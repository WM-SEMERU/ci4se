def makeLinearcFunc(self, mNrm, cNrm):
    cFuncUnc = LinearInterp(mNrm, cNrm, self.MPCminNow_j * self.hNrmNow_j,
        self.MPCminNow_j)
    return cFuncUnc