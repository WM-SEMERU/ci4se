def _evaluate(self, R, z, phi=0.0, t=0.0):
    if not self.HernquistSelf == None:
        return self.HernquistSelf._evaluate(R, z, phi=phi, t=t)
    elif not self.JaffeSelf == None:
        return self.JaffeSelf._evaluate(R, z, phi=phi, t=t)
    elif not self.NFWSelf == None:
        return self.NFWSelf._evaluate(R, z, phi=phi, t=t)
    else:
        return TwoPowerSphericalPotential._evaluate(self, R, z, phi=phi, t=
            t, _forceFloatEval=True)