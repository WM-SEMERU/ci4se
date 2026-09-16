def fits_region_objects_to_table(regions):
    for reg in regions:
        if isinstance(reg, SkyRegion):
            raise TypeError('Every region must be a pixel region'.format(reg))
    shape_list = to_shape_list(regions, coordinate_system='image')
    return shape_list.to_fits()