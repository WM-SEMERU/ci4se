def encode_multiple_layers(out, features_by_layer, zoom):
    precision = precision_for_zoom(zoom)
    geojson = {}
    for layer_name, features in features_by_layer.items():
        fs = create_layer_feature_collection(features, precision)
        geojson[layer_name] = fs
    json.dump(geojson, out)