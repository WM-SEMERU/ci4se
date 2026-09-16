def _z2deriv(self, R, z, phi=0.0, t=0.0):
    return self._mn3[0].z2deriv(R, z, phi=phi, t=t) + self._mn3[1].z2deriv(R,
        z, phi=phi, t=t) + self._mn3[2].z2deriv(R, z, phi=phi, t=t)