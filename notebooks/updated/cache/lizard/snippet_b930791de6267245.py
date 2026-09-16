def _compute_C_matrix(self):
    self.C = np.repeat(np.diag(self.Lp)[:, (np.newaxis)], self.Lp.shape[0],
        axis=1)
    self.C += np.repeat(np.diag(self.Lp)[(np.newaxis), :], self.Lp.shape[0],
        axis=0)
    self.C -= 2 * self.Lp
    volG = np.sum(self.z)
    self.C *= volG
    settings.mt(0, 'computed commute distance matrix')
    self.distances_dpt = self.C