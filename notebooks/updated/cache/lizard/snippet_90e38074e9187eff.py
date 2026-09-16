def _parse_list(features, new_names):
    feature_collection = OrderedDict()
    for feature in features:
        if isinstance(feature, FeatureType):
            feature_collection[feature] = ...
        elif isinstance(feature, (tuple, list)):
            for feature_type, feature_dict in FeatureParser._parse_tuple(
                feature, new_names).items():
                feature_collection[feature_type] = feature_collection.get(
                    feature_type, OrderedDict())
                if feature_dict is ...:
                    feature_collection[feature_type] = ...
                if feature_collection[feature_type] is not ...:
                    feature_collection[feature_type].update(feature_dict)
        else:
            raise ValueError('Failed to parse {}, expected a tuple'.format(
                feature))
    return feature_collection