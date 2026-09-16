def select_action(self, q_values):
    assert q_values.ndim == 1
    action = np.argmax(q_values)
    return action