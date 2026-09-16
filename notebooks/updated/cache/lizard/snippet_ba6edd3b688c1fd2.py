def split(input_file, file_1, file_2, no_in_first_file):
    with open(input_file) as f:
        feat_collection = geojson.load(f)
    features = feat_collection['features']
    feat_collection_1 = geojson.FeatureCollection(features[0:no_in_first_file])
    feat_collection_2 = geojson.FeatureCollection(features[no_in_first_file:])
    with open(file_1, 'w') as f:
        geojson.dump(feat_collection_1, f)
    with open(file_2, 'w') as f:
        geojson.dump(feat_collection_2, f)