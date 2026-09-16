def update(self):
    con = self.subpars.pars.control
    der = self.subpars
    for toy, qs in con.q:
        setattr(self, str(toy), 2.0 * con.v + der.seconds / der.nmbsubsteps *
            qs)
    self.refresh()