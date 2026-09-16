def _create_B(self, Y):
    Z = self._create_Z(Y)
    return np.dot(np.dot(Y, np.transpose(Z)), np.linalg.inv(np.dot(Z, np.
        transpose(Z))))