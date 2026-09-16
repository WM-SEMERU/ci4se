def rsdl_s(self, Yprev, Y):
    return self.rho * np.linalg.norm(self.cnst_AT(self.U))