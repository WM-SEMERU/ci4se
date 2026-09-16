def from_shapely(sgeom, srid=None):
    if SHAPELY:
        WKBWriter.defaults['include_srid'] = True
        if srid:
            lgeos.GEOSSetSRID(sgeom._geom, srid)
        return Geometry(sgeom.wkb_hex)
    else:
        raise DependencyError('Shapely')