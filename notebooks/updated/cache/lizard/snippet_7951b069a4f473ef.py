def from_geojson(geojson, srid=4326):
    type_ = geojson['type'].lower()
    if type_ == 'geometrycollection':
        geometries = []
        for geometry in geojson['geometries']:
            geometries.append(Geometry.from_geojson(geometry, srid=None))
        return GeometryCollection(geometries, srid)
    elif type_ == 'point':
        return Point(geojson['coordinates'], srid=srid)
    elif type_ == 'linestring':
        return LineString(geojson['coordinates'], srid=srid)
    elif type_ == 'polygon':
        return Polygon(geojson['coordinates'], srid=srid)
    elif type_ == 'multipoint':
        geometries = _MultiGeometry._multi_from_geojson(geojson, Point)
        return MultiPoint(geometries, srid=srid)
    elif type_ == 'multilinestring':
        geometries = _MultiGeometry._multi_from_geojson(geojson, LineString)
        return MultiLineString(geometries, srid=srid)
    elif type_ == 'multipolygon':
        geometries = _MultiGeometry._multi_from_geojson(geojson, Polygon)
        return MultiPolygon(geometries, srid=srid)