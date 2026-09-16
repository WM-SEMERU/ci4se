def major_rise_per_monomer(self):
    return numpy.cos(numpy.deg2rad(self.curve.alpha)
        ) * self.minor_rise_per_residue