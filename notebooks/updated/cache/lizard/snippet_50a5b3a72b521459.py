def D_d(self, H_0, Om0, Ode0=None):
    lensCosmo = self._get_cosom(H_0, Om0, Ode0)
    return lensCosmo.D_d