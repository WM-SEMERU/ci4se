def build_stops(pfeed, shapes=None):
    if pfeed.stops is not None:
        stops = pfeed.stops.copy()
    else:
        if shapes is None:
            raise ValueError('Must input shapes built by build_shapes()')
        geo_shapes = gt.geometrize_shapes(shapes)
        rows = []
        for shape, geom in geo_shapes[['shape_id', 'geometry']].itertuples(
            index=False):
            stop_ids = build_stop_ids(shape)
            stop_names = build_stop_names(shape)
            for i in range(2):
                stop_id = stop_ids[i]
                stop_name = stop_names[i]
                stop_lon, stop_lat = geom.interpolate(i, normalized=True
                    ).coords[0]
                rows.append([stop_id, stop_name, stop_lon, stop_lat])
        stops = pd.DataFrame(rows, columns=['stop_id', 'stop_name',
            'stop_lon', 'stop_lat']).drop_duplicates(subset=['stop_lon',
            'stop_lat'])
    return stops