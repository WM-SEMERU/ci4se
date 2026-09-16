def get_momentum_by_name(self, name):
    if name is None:
        raise TypeError("'name' should not be None")
    for momentum in self.momenta:
        if momentum.name == name:
            return momentum
    raise KeyError('No such momentum named {0}'.format(name))