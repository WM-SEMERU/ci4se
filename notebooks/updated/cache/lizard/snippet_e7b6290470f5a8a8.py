def calc_tmean_v1(self):
    con = self.parameters.control.fastaccess
    der = self.parameters.derived.fastaccess
    flu = self.sequences.fluxes.fastaccess
    flu.tmean = 0.0
    for k in range(con.nmbzones):
        flu.tmean += der.relzonearea[k] * flu.tc[k]