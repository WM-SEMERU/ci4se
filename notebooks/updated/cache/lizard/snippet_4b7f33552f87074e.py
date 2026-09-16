def get_potential_energy(self, a=None):
    if a is None:
        a = self.a
    if self.mask is None:
        return -np.sum(np.dot(a.get_positions()[self.mask], self.force))
    else:
        return -np.sum(np.dot(a.get_positions(), self.force))