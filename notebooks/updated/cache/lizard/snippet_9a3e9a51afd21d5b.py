def prob_from_sample(self, state, sample=None, window_size=None):
    if sample is None:
        sample = self.sample(self.random_state(), size=10000)
    if window_size is None:
        window_size = len(sample) // 100
    windows = len(sample) // window_size
    probabilities = np.zeros(windows)
    for i in range(windows):
        for j in range(window_size):
            ind = i * window_size + j
            state_eq = [(sample.loc[ind, v] == s) for v, s in state]
            if all(state_eq):
                probabilities[i] += 1
    return probabilities / window_size