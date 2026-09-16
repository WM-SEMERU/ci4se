def __densify_border(self):
    if isinstance(self._input_geom, MultiPolygon):
        polygons = [polygon for polygon in self._input_geom]
    else:
        polygons = [self._input_geom]
    points = []
    for polygon in polygons:
        if len(polygon.interiors) == 0:
            exterior = LineString(polygon.exterior)
            points += self.__fixed_interpolation(exterior)
        else:
            exterior = LineString(polygon.exterior)
            points += self.__fixed_interpolation(exterior)
            for j in range(len(polygon.interiors)):
                interior = LineString(polygon.interiors[j])
                points += self.__fixed_interpolation(interior)
    return points