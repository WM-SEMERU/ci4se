def _set_translations(self):
    pcell = PhonopyAtoms(numbers=[1], scaled_positions=[[0, 0, 0]], cell=np
        .diag([1, 1, 1]))
    smat = self._supercell_matrix
    self._trans_s = get_supercell(pcell, smat).get_scaled_positions()
    self._trans_p = np.dot(self._trans_s, self._supercell_matrix.T)
    self._N = len(self._trans_s)