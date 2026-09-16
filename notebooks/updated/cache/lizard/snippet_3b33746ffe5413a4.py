def _reassign_quantity_indexer(data, indexers):

    def _to_magnitude(val, unit):
        try:
            return val.to(unit).m
        except AttributeError:
            return val
    for coord_name in indexers:
        if (isinstance(data, xr.DataArray) and coord_name not in data.dims and
            coord_name in readable_to_cf_axes):
            axis = coord_name
            coord_name = next(data.metpy.coordinates(axis)).name
            indexers[coord_name] = indexers[axis]
            del indexers[axis]
        if isinstance(indexers[coord_name], slice):
            start = _to_magnitude(indexers[coord_name].start, data[
                coord_name].metpy.units)
            stop = _to_magnitude(indexers[coord_name].stop, data[coord_name
                ].metpy.units)
            step = _to_magnitude(indexers[coord_name].step, data[coord_name
                ].metpy.units)
            indexers[coord_name] = slice(start, stop, step)
        indexers[coord_name] = _to_magnitude(indexers[coord_name], data[
            coord_name].metpy.units)
    return indexers