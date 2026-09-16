def calc_qm_v1(self):
    con = self.parameters.control.fastaccess
    flu = self.sequences.fluxes.fastaccess
    if flu.am > 0.0 and flu.um > 0.0:
        flu.qm = con.ekm * con.skm * flu.am ** (5.0 / 3.0) / flu.um ** (2.0 /
            3.0) * con.gef ** 0.5
    else:
        flu.qm = 0.0