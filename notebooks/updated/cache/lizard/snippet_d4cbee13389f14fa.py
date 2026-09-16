def equation(self):
    mat = np.empty((self.nunknowns, self.model.neq))
    rhs = np.zeros(self.nunknowns)
    for icp in range(self.ncp):
        istart = icp * self.nlayers
        ieq = 0
        for e in self.model.elementlist:
            if e.nunknowns > 0:
                qx, qy = e.disvecinflayers(self.xcout[icp], self.ycout[icp],
                    self.layers)
                mat[istart:istart + self.nlayers, ieq:ieq + e.nunknowns
                    ] = qx * self.cosnorm[icp] + qy * self.sinnorm[icp]
                ieq += e.nunknowns
            else:
                qx, qy = e.disveclayers(self.xcout[icp], self.ycout[icp],
                    self.layers)
                rhs[istart:istart + self.nlayers] -= qx * self.cosnorm[icp
                    ] + qy * self.sinnorm[icp]
    return mat, rhs