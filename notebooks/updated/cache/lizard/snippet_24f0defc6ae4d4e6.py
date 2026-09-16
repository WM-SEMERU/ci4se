def modify_qa_v1(self):
    con = self.parameters.control.fastaccess
    der = self.parameters.derived.fastaccess
    flu = self.sequences.fluxes.fastaccess
    idx = der.toy[self.idx_sim]
    flu.qa = max(flu.qa - con.verzw[idx], 0.0)