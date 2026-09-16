def coord_to_dimension(coord):
    kwargs = {}
    if coord.units.is_time_reference():
        kwargs['value_format'] = get_date_format(coord)
    else:
        kwargs['unit'] = str(coord.units)
    return Dimension(coord.name(), **kwargs)