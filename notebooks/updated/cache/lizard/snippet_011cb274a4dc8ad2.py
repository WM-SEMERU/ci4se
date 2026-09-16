def epsg_code(geojson):
    if isinstance(geojson, dict):
        if 'crs' in geojson:
            urn = geojson['crs']['properties']['name'].split(':')
            if 'EPSG' in urn:
                try:
                    return int(urn[-1])
                except (TypeError, ValueError):
                    return None
    return None