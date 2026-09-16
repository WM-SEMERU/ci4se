def compute_greedy(self, v, sigma=None):
    if sigma is None:
        sigma = np.empty(self.num_states, dtype=int)
    self.bellman_operator(v, sigma=sigma)
    return sigma