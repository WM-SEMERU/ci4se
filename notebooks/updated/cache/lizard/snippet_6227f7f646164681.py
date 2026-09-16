def calc_requiredrelease_v1(self):
    con = self.parameters.control.fastaccess
    der = self.parameters.derived.fastaccess
    flu = self.sequences.fluxes.fastaccess
    flu.requiredrelease = con.neardischargeminimumthreshold[der.toy[self.
        idx_sim]]
    flu.requiredrelease = flu.requiredrelease + smoothutils.smooth_logistic2(
        flu.requiredremoterelease - flu.requiredrelease, der.
        neardischargeminimumsmoothpar2[der.toy[self.idx_sim]])