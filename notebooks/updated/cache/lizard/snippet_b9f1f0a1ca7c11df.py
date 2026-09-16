def eps_greedy(self, params):
    if params and type(params) == dict:
        eps = params.get('epsilon')
    else:
        eps = 0.1
    r = np.random.rand()
    if r < eps:
        return np.random.choice(list(set(range(len(self.wins))) - {self.
            max_mean()}))
    else:
        return self.max_mean()