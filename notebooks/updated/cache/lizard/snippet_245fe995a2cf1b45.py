def prepare_geojson(geojson):
    geojson = deepcopy(geojson)
    if geojson['type'] == 'Feature':
        geojson = geojson['geometry']
        if hasattr(geojson, 'properties'):
            del geojson['properties']
    if geojson['type'] == 'FeatureCollection':
        geojson['type'] = 'GeometryCollection'
        geojson['geometries'] = [feature['geometry'] for feature in geojson
            ['features']]
        del geojson['features']
    return geojson