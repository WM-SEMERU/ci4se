def block_sep1(self, Y):
    Y1 = Y[(...), self.cri.M:]
    if self.cri.Cd > 1:
        shp = list(Y1.shape)
        shp[self.cri.axisM] = self.cri.dimN
        shp[self.cri.axisC] = self.cri.Cd
        Y1 = Y1.reshape(shp)
    Y1 = np.swapaxes(Y1[..., np.newaxis], self.cri.axisM, -1)
    return Y1