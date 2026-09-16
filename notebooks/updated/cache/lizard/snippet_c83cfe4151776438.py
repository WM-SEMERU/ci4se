def _get_v(self, rho):
    v_mol = self.mass / rho
    v = vol_mol2uc(v_mol * 1e-06, self.z)
    print(v)
    return v