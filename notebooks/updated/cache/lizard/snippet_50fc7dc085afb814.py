def sde(self):
    variance = float(self.variance.values)
    lengthscale = float(self.lengthscale)
    F = np.array(((-1.0 / lengthscale,),))
    L = np.array(((1.0,),))
    Qc = np.array(((2.0 * variance / lengthscale,),))
    H = np.array(((1.0,),))
    Pinf = np.array(((variance,),))
    P0 = Pinf.copy()
    dF = np.zeros((1, 1, 2))
    dQc = np.zeros((1, 1, 2))
    dPinf = np.zeros((1, 1, 2))
    dF[:, :, (0)] = 0.0
    dF[:, :, (1)] = 1.0 / lengthscale ** 2
    dQc[:, :, (0)] = 2.0 / lengthscale
    dQc[:, :, (1)] = -2.0 * variance / lengthscale ** 2
    dPinf[:, :, (0)] = 1.0
    dPinf[:, :, (1)] = 0.0
    dP0 = dPinf.copy()
    return F, L, Qc, H, Pinf, P0, dF, dQc, dPinf, dP0