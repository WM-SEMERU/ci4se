def load_configs(self, filename):
    configs = np.loadtxt(filename)
    self.add_to_configs(configs)