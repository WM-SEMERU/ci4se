def update(self):
    con = self.subpars.pars.control
    self(0.0)
    for idx in range(2):
        if con.bbv[idx] > 0.0 and con.bnv[idx] > 0.0:
            self.values[idx] = con.bbv[idx] / con.bnv[idx]