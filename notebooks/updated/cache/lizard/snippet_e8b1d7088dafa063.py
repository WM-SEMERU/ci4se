def get_doping(self, fermi, T):
    cb_integral = np.sum(self.tdos[self.idx_cbm:] * f0(self.energies[self.
        idx_cbm:], fermi, T) * self.de[self.idx_cbm:], axis=0)
    vb_integral = np.sum(self.tdos[:self.idx_vbm + 1] * (1 - f0(self.
        energies[:self.idx_vbm + 1], fermi, T)) * self.de[:self.idx_vbm + 1
        ], axis=0)
    return (vb_integral - cb_integral) / (self.volume * self.A_to_cm ** 3)