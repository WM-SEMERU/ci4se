def reset_params(self):
    self.__params = dict([p, None] for p in self.param_names)
    self.set_params(self.param_defaults)