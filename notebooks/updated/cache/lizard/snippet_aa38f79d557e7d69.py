def get_area_slices(data_area, area_to_cover):
    if data_area.proj_dict['proj'] != 'geos':
        raise NotImplementedError('Only geos supported')
    if area_to_cover.proj_dict['proj'] == data_area.proj_dict['proj']:
        LOGGER.debug('Projections for data and slice areas are identical: {}'
            .format(area_to_cover.proj_dict['proj']))
        llx, lly, urx, ury = area_to_cover.area_extent
        x, y = data_area.get_xy_from_proj_coords([llx, urx], [lly, ury])
        return slice(x[0], x[1] + 1), slice(y[1], y[0] + 1)
    data_boundary = Boundary(*get_geostationary_bounding_box(data_area))
    area_boundary = AreaDefBoundary(area_to_cover, 100)
    intersection = data_boundary.contour_poly.intersection(area_boundary.
        contour_poly)
    x, y = data_area.get_xy_from_lonlat(np.rad2deg(intersection.lon), np.
        rad2deg(intersection.lat))
    return slice(min(x), max(x) + 1), slice(min(y), max(y) + 1)