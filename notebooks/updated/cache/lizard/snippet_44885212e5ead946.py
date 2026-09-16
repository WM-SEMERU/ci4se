def get_grid_district_polygon(config, subst_id=None, projection=4326):
    conn = connection(section=config['db_connection']['section'])
    Session = sessionmaker(bind=conn)
    session = Session()
    if config['data_source']['oedb_data_source'] == 'versioned':
        version = config['versioned']['version']
        query = session.query(EgoDpMvGriddistrict.subst_id,
            EgoDpMvGriddistrict.geom)
        Regions = [(subst_id, shape.to_shape(geom)) for subst_id, geom in
            query.filter(EgoDpMvGriddistrict.version == version, 
            EgoDpMvGriddistrict.subst_id == subst_id).all()]
    else:
        query = session.query(EgoGridMvGriddistrict.subst_id,
            EgoGridMvGriddistrict.geom)
        Regions = [(subst_id, shape.to_shape(geom)) for subst_id, geom in
            query.filter(EgoGridMvGriddistrict.subst_id.in_(subst_id)).all()]
    crs = {'init': 'epsg:3035'}
    region = gpd.GeoDataFrame(Regions, columns=['subst_id', 'geometry'],
        crs=crs)
    region = region.to_crs(epsg=projection)
    return region