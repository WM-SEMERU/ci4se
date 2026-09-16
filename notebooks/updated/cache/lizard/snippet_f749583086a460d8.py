def select_action(self, q_values):
    assert q_values.ndim == 1
    nb_actions = q_values.shape[0]
    if np.random.uniform() < self.eps:
        action = np.random.randint(0, nb_actions)
    else:
        action = np.argmax(q_values)
    return action