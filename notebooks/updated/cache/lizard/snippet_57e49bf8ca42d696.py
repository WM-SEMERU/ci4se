def derivativeY(self, w, x, y, z):
    wa = np.asarray(w)
    xa = np.asarray(x)
    ya = np.asarray(y)
    za = np.asarray(z)
    return self._derY(wa.flatten(), xa.flatten(), ya.flatten(), za.flatten()
        ).reshape(wa.shape)