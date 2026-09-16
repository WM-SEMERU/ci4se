def compute_residuals(self):
    if self.opt['AutoRho', 'StdResiduals']:
        r = np.linalg.norm(self.rsdl_r(self.AXnr, self.Y))
        s = np.linalg.norm(self.rsdl_s(self.Yprev, self.Y))
        epri = np.sqrt(self.Nc) * self.opt['AbsStopTol'] + self.rsdl_rn(self
            .AXnr, self.Y) * self.opt['RelStopTol']
        edua = np.sqrt(self.Nx) * self.opt['AbsStopTol'] + self.rsdl_sn(self.U
            ) * self.opt['RelStopTol']
    else:
        rn = self.rsdl_rn(self.AXnr, self.Y)
        if rn == 0.0:
            rn = 1.0
        sn = self.rsdl_sn(self.U)
        if sn == 0.0:
            sn = 1.0
        r = np.linalg.norm(self.rsdl_r(self.AXnr, self.Y)) / rn
        s = np.linalg.norm(self.rsdl_s(self.Yprev, self.Y)) / sn
        epri = np.sqrt(self.Nc) * self.opt['AbsStopTol'] / rn + self.opt[
            'RelStopTol']
        edua = np.sqrt(self.Nx) * self.opt['AbsStopTol'] / sn + self.opt[
            'RelStopTol']
    return r, s, epri, edua