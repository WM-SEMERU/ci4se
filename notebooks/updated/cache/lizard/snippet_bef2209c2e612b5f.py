def parameters(self):
    length_a = np.linalg.norm(self.matrix[:, (0)])
    length_b = np.linalg.norm(self.matrix[:, (1)])
    length_c = np.linalg.norm(self.matrix[:, (2)])
    alpha = np.arccos(np.dot(self.matrix[:, (1)], self.matrix[:, (2)]) / (
        length_b * length_c))
    beta = np.arccos(np.dot(self.matrix[:, (2)], self.matrix[:, (0)]) / (
        length_c * length_a))
    gamma = np.arccos(np.dot(self.matrix[:, (0)], self.matrix[:, (1)]) / (
        length_a * length_b))
    return np.array([length_a, length_b, length_c], float), np.array([alpha,
        beta, gamma], float)