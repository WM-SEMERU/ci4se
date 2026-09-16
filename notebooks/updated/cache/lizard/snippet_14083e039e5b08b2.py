def possible_params(self):
    return self.params if isinstance(self.params, list) else [self.params]