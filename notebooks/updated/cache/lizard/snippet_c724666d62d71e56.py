def get_seed_sub(self, label):
    sx, sy, sz = np.nonzero(self.seeds == label)
    return sx, sy, sz