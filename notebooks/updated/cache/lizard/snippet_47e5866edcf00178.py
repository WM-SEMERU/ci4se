def get_frequencies(self, q):
    self._set_dynamical_matrix()
    if self._dynamical_matrix is None:
        msg = 'Dynamical matrix has not yet built.'
        raise RuntimeError(msg)
    self._dynamical_matrix.set_dynamical_matrix(q)
    dm = self._dynamical_matrix.get_dynamical_matrix()
    frequencies = []
    for eig in np.linalg.eigvalsh(dm).real:
        if eig < 0:
            frequencies.append(-np.sqrt(-eig))
        else:
            frequencies.append(np.sqrt(eig))
    return np.array(frequencies) * self._factor