def rsdl_rn(self, AX, Y):
    if not hasattr(self, '_cnst_nrm_c'):
        self._cnst_nrm_c = np.sqrt(np.linalg.norm(self.cnst_c0()) ** 2 + np
            .linalg.norm(self.cnst_c1()) ** 2)
    return max((np.linalg.norm(AX), np.linalg.norm(Y), self._cnst_nrm_c))