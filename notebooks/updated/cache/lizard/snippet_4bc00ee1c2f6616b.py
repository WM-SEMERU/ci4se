def sample(self, k=None, with_replacement=True, weights=None):
    n = self.num_rows
    if k is None:
        k = n
    index = np.random.choice(n, k, replace=with_replacement, p=weights)
    columns = [[c[i] for i in index] for c in self.columns]
    sample = self._with_columns(columns)
    return sample