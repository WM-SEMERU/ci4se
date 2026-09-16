def from_coords(cls, coords, sort=True):
    coords = list(coords)
    if sort:
        coords.sort()
    if len(coords[0]) == 2:
        lons, lats = zip(*coords)
        depths = None
    else:
        lons, lats, depths = zip(*coords)
        depths = numpy.array(depths)
    return cls(numpy.array(lons), numpy.array(lats), depths)