def _get_sm_scale_in(self, scale_sm=91.1876):
    _smeft = SMEFT()
    _smeft.set_initial(self.C_in, self.scale_in, self.scale_high)
    _smeft.C_in.update(self._run_sm_scale_in(self.C_in, scale_sm=scale_sm))
    C_out = _smeft.rgevolve_leadinglog(scale_sm)
    return self._run_sm_scale_in(C_out, scale_sm=scale_sm)