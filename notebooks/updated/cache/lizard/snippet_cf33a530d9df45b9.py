def setup(self):
    super(RogersExperiment, self).setup()
    for net in random.sample(self.networks(role='experiment'), self.
        catch_repeats):
        net.role = 'catch'
    for net in self.networks():
        source = RogersSource(network=net)
        source.create_information()
        if net.role == 'practice':
            env = RogersEnvironment(network=net)
            env.create_state(proportion=self.practice_difficulty)
        if net.role == 'catch':
            env = RogersEnvironment(network=net)
            env.create_state(proportion=self.catch_difficulty)
        if net.role == 'experiment':
            difficulty = self.difficulties[self.networks(role='experiment')
                .index(net)]
            env = RogersEnvironment(network=net)
            env.create_state(proportion=difficulty)