def parameter_init(self, name, shape, init):
    p = self.params.get(name, shape=shape, init=init)
    return p