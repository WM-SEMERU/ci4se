def _init_network(self):
    self.network = Network(self.problem.layers)
    self.weights = Matrices(self.network.shapes)
    if self.load:
        loaded = np.load(self.load)
        assert loaded.shape == self.weights.shape, 'weights to load must match problem definition'
        self.weights.flat = loaded
    else:
        self.weights.flat = np.random.normal(self.problem.weight_mean, self
            .problem.weight_scale, len(self.weights.flat))