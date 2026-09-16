def cal_pth(self, v, temp):
    if self.eqn_th is None or self.params_th is None:
        return np.zeros_like(v)
    params = self._set_params(self.params_th)
    return func_th[self.eqn_th](v, temp, *params, self.n, self.z, t_ref=
        self.t_ref, three_r=self.three_r)