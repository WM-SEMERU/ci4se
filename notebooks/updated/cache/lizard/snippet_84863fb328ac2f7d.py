def xstep(self):
    self.YU1[:] = self.Y1 - self.U1
    self.ZSf = np.conj(self.Zf) * (self.Sf + sl.rfftn(self.YU1, None, self.
        cri.axisN))
    rho = self.rho
    self.rho = 1.0
    super(ConvCnstrMODMaskDcpl_Consensus, self).xstep()
    self.rho = rho