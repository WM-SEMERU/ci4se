def add(self, sim, module, package=None):
    super(Simulations, self).add(sim, module, package)
    if sim not in self.layer:
        self.layer[sim] = {'module': module, 'package': package}