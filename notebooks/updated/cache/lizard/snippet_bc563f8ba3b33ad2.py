def get_normalized_elevation_array(world):
    e = world.layers['elevation'].data
    ocean = world.layers['ocean'].data
    mask = numpy.ma.array(e, mask=ocean)
    min_elev_land = mask.min()
    max_elev_land = mask.max()
    elev_delta_land = max_elev_land - min_elev_land
    mask = numpy.ma.array(e, mask=numpy.logical_not(ocean))
    min_elev_sea = mask.min()
    max_elev_sea = mask.max()
    elev_delta_sea = max_elev_sea - min_elev_sea
    c = numpy.empty(e.shape, dtype=numpy.float)
    c[numpy.invert(ocean)] = (e[numpy.invert(ocean)] - min_elev_land
        ) * 127 / elev_delta_land + 128
    c[ocean] = (e[ocean] - min_elev_sea) * 127 / elev_delta_sea
    c = numpy.rint(c).astype(dtype=numpy.int32)
    return c