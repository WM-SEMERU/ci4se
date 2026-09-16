def gen_reciprocals(self, append=False):
    reciprocals = self.configs.copy()[:, ::-1]
    reciprocals[:, 0:2] = np.sort(reciprocals[:, 0:2], axis=1)
    reciprocals[:, 2:4] = np.sort(reciprocals[:, 2:4], axis=1)
    ind = np.lexsort((reciprocals[:, (3)], reciprocals[:, (2)], reciprocals
        [:, (1)], reciprocals[:, (0)]))
    reciprocals = reciprocals[ind]
    if append:
        self.configs = np.vstack((self.configs, reciprocals))
    return reciprocals