def get_surface_boundaries(self):
    mesh = self.mesh
    lons = numpy.concatenate((mesh.lons[(0), :], mesh.lons[1:, (-1)], mesh.
        lons[(-1), :-1][::-1], mesh.lons[:-1, (0)][::-1]))
    lats = numpy.concatenate((mesh.lats[(0), :], mesh.lats[1:, (-1)], mesh.
        lats[(-1), :-1][::-1], mesh.lats[:-1, (0)][::-1]))
    return [lons], [lats]