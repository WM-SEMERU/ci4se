def features_keep_using_features(obj, bounds):
    bounds_shapes = [(feature, shapely.geometry.shape(feature['geometry'])) for
        feature in tqdm(bounds['features']) if feature['geometry'] is not None]
    index = rtree.index.Index()
    for i in tqdm(range(len(bounds_shapes))):
        feature, shape = bounds_shapes[i]
        index.insert(i, shape.bounds)
    features_keep = []
    for feature in tqdm(obj['features']):
        if 'geometry' in feature and 'coordinates' in feature['geometry']:
            coordinates = feature['geometry']['coordinates']
            if any([shape.contains(shapely.geometry.Point(lon, lat)) for 
                lon, lat in coordinates for feature, shape in [
                bounds_shapes[i] for i in index.nearest((lon, lat, lon, lat
                ), 1)]]):
                features_keep.append(feature)
                continue
    obj['features'] = features_keep
    return obj