def _update_params(self, constants):
    for k, v in constants.items():
        self.params[k]['value'] *= v
    influence = self._calculate_influence(self.params['infl']['value'])
    return influence * self.params['lr']['value']