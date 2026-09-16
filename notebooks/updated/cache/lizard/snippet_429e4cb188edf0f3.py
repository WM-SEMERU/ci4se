def azimuth(lons1, lats1, lons2, lats2):
    lons1, lats1, lons2, lats2 = _prepare_coords(lons1, lats1, lons2, lats2)
    cos_lat2 = numpy.cos(lats2)
    true_course = numpy.degrees(numpy.arctan2(numpy.sin(lons1 - lons2) *
        cos_lat2, numpy.cos(lats1) * numpy.sin(lats2) - numpy.sin(lats1) *
        cos_lat2 * numpy.cos(lons1 - lons2)))
    return (360 - true_course) % 360