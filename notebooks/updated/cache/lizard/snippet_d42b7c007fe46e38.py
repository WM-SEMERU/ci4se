def get_dip(self):
    areas = self._get_areas()
    dips = numpy.array([surf.get_dip() for surf in self.surfaces])
    return numpy.sum(areas * dips) / numpy.sum(areas)