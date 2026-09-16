def conditional_probability_alive_matrix(self, max_frequency=None,
    max_recency=None):
    max_frequency = max_frequency or int(self.data['frequency'].max())
    max_recency = max_recency or int(self.data['T'].max())
    return np.fromfunction(self.conditional_probability_alive, (
        max_frequency + 1, max_recency + 1), T=max_recency).T