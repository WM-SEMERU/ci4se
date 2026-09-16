def get_ry0_distance(self, mesh):
    top_edge = self.mesh[0:1]
    mean_strike = self.get_strike()
    dst1 = geodetic.distance_to_arc(top_edge.lons[0, 0], top_edge.lats[0, 0
        ], (mean_strike + 90.0) % 360, mesh.lons, mesh.lats)
    dst2 = geodetic.distance_to_arc(top_edge.lons[0, -1], top_edge.lats[0, 
        -1], (mean_strike + 90.0) % 360, mesh.lons, mesh.lats)
    idx = numpy.sign(dst1) == numpy.sign(dst2)
    dst = numpy.zeros_like(dst1)
    dst[idx] = numpy.fmin(numpy.abs(dst1[idx]), numpy.abs(dst2[idx]))
    return dst