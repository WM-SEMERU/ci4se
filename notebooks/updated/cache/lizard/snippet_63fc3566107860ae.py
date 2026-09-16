def _parse_names_dict(feature_names):
    feature_collection = OrderedDict()
    for feature_name, new_feature_name in feature_names.items():
        if isinstance(feature_name, str) and (isinstance(new_feature_name,
            str) or new_feature_name is ...):
            feature_collection[feature_name] = new_feature_name
        elif not isinstance(feature_name, str):
            raise ValueError('Failed to parse {}, expected string'.format(
                feature_name))
        else:
            raise ValueError('Failed to parse {}, expected string or Ellipsis'
                .format(new_feature_name))
    return feature_collection