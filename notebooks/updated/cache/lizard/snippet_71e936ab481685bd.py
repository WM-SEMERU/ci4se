def trunc_neg_eigs(self, particle):
    arr = np.tensordot(particle, self._basis.data.conj(), 1)
    w, v = np.linalg.eig(arr)
    if np.all(w >= 0):
        return particle
    else:
        w[w < 0] = 0
        new_arr = np.dot(v * w, v.conj().T)
        new_particle = np.real(np.dot(self._basis.flat(), new_arr.flatten()))
        assert new_particle[0] > 0
        return new_particle