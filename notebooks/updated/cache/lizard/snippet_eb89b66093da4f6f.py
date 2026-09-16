def gradients_X(self, dL_dK, X, X2, target):
    if X2 == None or X2 is X:
        dL_dKdiag = dL_dK.flat[::dL_dK.shape[0] + 1]
        self.dKdiag_dX(dL_dKdiag, X, target)