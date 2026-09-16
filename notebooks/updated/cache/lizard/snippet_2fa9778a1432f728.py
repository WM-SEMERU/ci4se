def cal_pel(self, v, temp):
    if self.eqn_el is None or self.params_el is None:
        return np.zeros_like(v)
    params = self._set_params(self.params_el)
    return func_el[self.eqn_el](v, temp, *params, self.n, self.z, t_ref=
        self.t_ref, three_r=self.three_r)