def computeSVD(self, k, computeU=False, rCond=1e-09):
    j_model = self._java_matrix_wrapper.call('computeSVD', int(k), bool(
        computeU), float(rCond))
    return SingularValueDecomposition(j_model)