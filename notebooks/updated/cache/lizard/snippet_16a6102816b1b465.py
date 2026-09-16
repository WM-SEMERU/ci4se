def calc_nbes_inzp_v1(self):
    con = self.parameters.control.fastaccess
    der = self.parameters.derived.fastaccess
    flu = self.sequences.fluxes.fastaccess
    sta = self.sequences.states.fastaccess
    for k in range(con.nhru):
        if con.lnk[k] in (WASSER, FLUSS, SEE):
            flu.nbes[k] = 0.0
            sta.inzp[k] = 0.0
        else:
            flu.nbes[k] = max(flu.nkor[k] + sta.inzp[k] - der.kinz[con.lnk[
                k] - 1, der.moy[self.idx_sim]], 0.0)
            sta.inzp[k] += flu.nkor[k] - flu.nbes[k]