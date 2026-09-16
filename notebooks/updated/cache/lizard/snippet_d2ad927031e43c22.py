def reconstruct(self, D=None, X=None):
    if D is None:
        D = self.getdict(crop=False)
    if X is None:
        X = self.getcoef()
    Df = sl.rfftn(D, self.xstep.cri.Nv, self.xstep.cri.axisN)
    Xf = sl.rfftn(X, self.xstep.cri.Nv, self.xstep.cri.axisN)
    DXf = sl.inner(Df, Xf, axis=self.xstep.cri.axisM)
    return sl.irfftn(DXf, self.xstep.cri.Nv, self.xstep.cri.axisN)