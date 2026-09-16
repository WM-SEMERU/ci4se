def ystep(self):
    r
    self.Y = sp.proj_l1(self.AX + self.U, self.gamma, axis=self.cri.axisN +
        (self.cri.axisC, self.cri.axisM))
    super(ConvBPDNProjL1, self).ystep()