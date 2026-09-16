def fft_mesh(self, kpoint, band, spin=0, shift=True):
    mesh = np.zeros(tuple(self.ng), dtype=np.complex)
    tcoeffs = self.coeffs[spin][kpoint][band
        ] if self.spin == 2 else self.coeffs[kpoint][band]
    for gp, coeff in zip(self.Gpoints[kpoint], tcoeffs):
        t = tuple(gp.astype(np.int) + (self.ng / 2).astype(np.int))
        mesh[t] = coeff
    if shift:
        return np.fft.ifftshift(mesh)
    else:
        return mesh