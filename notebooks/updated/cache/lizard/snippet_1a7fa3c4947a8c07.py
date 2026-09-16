def dnde(self, x, params=None):
    params = self.params if params is None else params
    return np.squeeze(self.eval_dnde(x, params, self.scale, self.extra_params))