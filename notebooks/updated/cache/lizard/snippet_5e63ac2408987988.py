def _run_sm_scale_in(self, C_out, scale_sm=91.1876):
    smeft_sm = SMEFT()
    C_in_sm = beta.C_array2dict(np.zeros(9999))
    C_SM = smpar.smeftpar(scale_sm, self.scale_high, C_out, basis='Warsaw')
    C_SM = {k: v for k, v in C_SM.items() if k in definitions.SM_keys}
    C_in_sm.update(C_out)
    C_in_sm.update(C_SM)
    smeft_sm.set_initial(C_in_sm, scale_sm, scale_high=self.scale_high)
    C_SM_high = smeft_sm.rgevolve(self.scale_in, newphys=False, rtol=0.01,
        atol=1)
    return {k: v for k, v in C_SM_high.items() if k in definitions.SM_keys}