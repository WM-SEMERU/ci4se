def _J(self):
    pd = self.particle_distribution(self._Ep * u.GeV)
    return pd.to('1/GeV').value