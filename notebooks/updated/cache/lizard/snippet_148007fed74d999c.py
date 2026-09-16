def clean_boundary_shapefile(shapefile_path):
    wfg = gpd.read_file(shapefile_path)
    first_shape = wfg.iloc[0].geometry
    if hasattr(first_shape, 'geoms'):
        log.warning('MultiPolygon found in boundary. Picking largest area ...')
        max_area = -9999.0
        main_geom = None
        for geom in first_shape.geoms:
            if geom.area > max_area:
                main_geom = geom
                max_area = geom.area
        if not main_geom.is_valid:
            log.warning(
                'Invalid geometry found in boundary. Attempting to self clean ...'
                )
            main_geom = main_geom.buffer(0)
        wfg.loc[0, 'geometry'] = main_geom
        out_cleaned_boundary_shapefile = os.path.splitext(shapefile_path)[0
            ] + str(uuid.uuid4()) + '.shp'
        wfg.to_file(out_cleaned_boundary_shapefile)
        log.info('Cleaned boundary shapefile written to:{}'.format(
            out_cleaned_boundary_shapefile))
        return out_cleaned_boundary_shapefile
    return shapefile_path