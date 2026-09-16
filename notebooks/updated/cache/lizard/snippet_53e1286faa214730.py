def _update_B(self):
    for param in self.freeparams:
        if param == 'mu':
            continue
        paramval = getattr(self, param)
        if isinstance(paramval, float):
            self.B[param] = broadcastMatrixMultiply(self.Ainv,
                broadcastMatrixMultiply(self.dPrxy[param], self.A))
        else:
            assert isinstance(paramval, numpy.ndarray) and paramval.ndim == 1
            for j in range(paramval.shape[0]):
                self.B[param][j] = broadcastMatrixMultiply(self.Ainv,
                    broadcastMatrixMultiply(self.dPrxy[param][j], self.A))