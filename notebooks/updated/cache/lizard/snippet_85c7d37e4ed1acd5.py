def Ey(self, f):
    r
    return np.exp(f) if self.tranfcn == 'exp' else softplus(f)