def extractLargestSubNetwork(cls, network_file, out_subset_network_file,
    river_id_field, next_down_id_field, river_magnitude_field, safe_mode=True):
    network_shapefile = ogr.Open(network_file)
    network_layer = network_shapefile.GetLayer()
    number_of_features = network_layer.GetFeatureCount()
    riv_magnuitude_list = np.zeros(number_of_features, dtype=np.int32)
    for feature_idx, drainage_line_feature in enumerate(network_layer):
        riv_magnuitude_list[feature_idx] = drainage_line_feature.GetField(
            river_magnitude_field)
    max_magnitude_feature = network_layer.GetFeature(np.argmax(
        riv_magnuitude_list))
    cls.extractSubNetwork(network_file, out_subset_network_file, [
        max_magnitude_feature.GetField(river_id_field)], river_id_field,
        next_down_id_field, river_magnitude_field, safe_mode)