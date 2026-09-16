def _dump_geometrycollection(obj, decimals):
    gc = 'GEOMETRYCOLLECTION (%s)'
    geoms = obj['geometries']
    geoms_wkt = []
    for geom in geoms:
        geom_type = geom['type']
        geoms_wkt.append(_dumps_registry.get(geom_type)(geom, decimals))
    gc %= ','.join(geoms_wkt)
    return gc