def obfn_g0var(self):
    return self.var_y0() if self.opt['gEvalY'] else self.block_sep0(self.AXnr)