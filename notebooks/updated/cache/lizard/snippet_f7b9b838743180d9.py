def dumps(obj, decimals=16):
    try:
        geom_type = obj['type']
        exporter = _dumps_registry.get(geom_type)
        if exporter is None:
            _unsupported_geom_type(geom_type)
        if geom_type == 'GeometryCollection':
            if len(obj['geometries']) == 0:
                return 'GEOMETRYCOLLECTION EMPTY'
        elif len(list(util.flatten_multi_dim(obj['coordinates']))) == 0:
            return '%s EMPTY' % geom_type.upper()
    except KeyError:
        raise geomet.InvalidGeoJSONException('Invalid GeoJSON: %s' % obj)
    result = exporter(obj, decimals)
    meta_srid = obj.get('meta', {}).get('srid')
    crs_srid = obj.get('crs', {}).get('properties', {}).get('name')
    if crs_srid is not None:
        crs_srid = crs_srid.replace('EPSG', '')
    if meta_srid is not None and crs_srid is not None and str(meta_srid
        ) != str(crs_srid):
        raise ValueError('Ambiguous CRS/SRID values: %s and %s' % (
            meta_srid, crs_srid))
    srid = meta_srid or crs_srid
    if srid is not None:
        result = 'SRID=%s;%s' % (srid, result)
    return result