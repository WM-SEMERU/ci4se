def project_gdf(gdf, to_crs=None, to_latlong=False):
    assert len(gdf) > 0, 'You cannot project an empty GeoDataFrame.'
    start_time = time.time()
    if not hasattr(gdf, 'gdf_name'):
        gdf.gdf_name = 'unnamed'
    if to_crs is not None:
        projected_gdf = gdf.to_crs(to_crs)
    elif to_latlong:
        latlong_crs = settings.default_crs
        projected_gdf = gdf.to_crs(latlong_crs)
        log('Projected the GeoDataFrame "{}" to default_crs in {:,.2f} seconds'
            .format(gdf.gdf_name, time.time() - start_time))
    else:
        if gdf.crs is not None and 'proj' in gdf.crs and gdf.crs['proj'
            ] == 'utm':
            return gdf
        avg_longitude = gdf['geometry'].unary_union.centroid.x
        utm_zone = int(math.floor((avg_longitude + 180) / 6.0) + 1)
        utm_crs = {'datum': 'WGS84', 'ellps': 'WGS84', 'proj': 'utm',
            'zone': utm_zone, 'units': 'm'}
        projected_gdf = gdf.to_crs(utm_crs)
        log('Projected the GeoDataFrame "{}" to UTM-{} in {:,.2f} seconds'.
            format(gdf.gdf_name, utm_zone, time.time() - start_time))
    projected_gdf.gdf_name = gdf.gdf_name
    return projected_gdf