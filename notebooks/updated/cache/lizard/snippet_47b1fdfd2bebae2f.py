def __create_proj_mat(self, size):
    s = 1 / self.density
    return np.random.choice([-np.sqrt(s / self.k), 0, np.sqrt(s / self.k)],
        size=size, p=[1 / (2 * s), 1 - 1 / s, 1 / (2 * s)])