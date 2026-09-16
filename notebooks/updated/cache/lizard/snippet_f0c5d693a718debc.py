def eval_objfn(self):
    fval = self.obfn_f(self.obfn_fvar())
    g0val = self.obfn_g0(self.obfn_g0var())
    g1val = self.obfn_g1(self.obfn_g1var())
    obj = fval + g0val + g1val
    return obj, fval, g0val, g1val