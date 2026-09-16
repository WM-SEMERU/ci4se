def select_action(self, q_values):
    assert self.agent.training, 'BoltzmannGumbelQPolicy should only be used for training, not testing'
    assert q_values.ndim == 1, q_values.ndim
    q_values = q_values.astype('float64')
    if self.agent.step == 0:
        self.action_counts = np.ones(q_values.shape)
    assert self.action_counts is not None, self.agent.step
    assert self.action_counts.shape == q_values.shape, (self.action_counts.
        shape, q_values.shape)
    beta = self.C / np.sqrt(self.action_counts)
    Z = np.random.gumbel(size=q_values.shape)
    perturbation = beta * Z
    perturbed_q_values = q_values + perturbation
    action = np.argmax(perturbed_q_values)
    self.action_counts[action] += 1
    return action