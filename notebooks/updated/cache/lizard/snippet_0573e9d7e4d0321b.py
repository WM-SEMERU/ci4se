def obfn_f(self, Xf=None):
    r
    if Xf is None:
        Xf = self.Xf
    Rf = self.eval_Rf(Xf)
    return 0.5 * np.linalg.norm(Rf.flatten(), 2) ** 2