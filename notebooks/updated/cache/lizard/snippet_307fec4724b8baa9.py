def cal_panh(self, v, temp):
    if self.eqn_anh is None or self.params_anh is None:
        return np.zeros_like(v)
    params = self._set_params(self.params_anh)
    return func_anh[self.eqn_anh](v, temp, *params, self.n, self.z, t_ref=
        self.t_ref, three_r=self.three_r)