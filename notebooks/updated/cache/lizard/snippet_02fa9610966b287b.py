def _select_valid_features(dataset, features, valid_feature_types,
    target_column=None):
    if features is not None:
        if not hasattr(features, '__iter__'):
            raise TypeError("Input 'features' must be an iterable type.")
        if not all([isinstance(x, str) for x in features]):
            raise TypeError("Input 'features' must contain only strings.")
    if features is None:
        features = dataset.column_names()
    col_type_map = {col_name: col_type for col_name, col_type in zip(
        dataset.column_names(), dataset.column_types())}
    valid_features = []
    for col_name in features:
        if col_name not in dataset.column_names():
            _logging.warning("Column '{}' is not in the input dataset.".
                format(col_name))
        elif col_name == target_column:
            _logging.warning('Excluding target column ' + target_column +
                ' as a feature.')
        elif col_type_map[col_name] not in valid_feature_types:
            _logging.warning("Column '{}' is excluded as a ".format(
                col_name) + 'feature due to invalid column type.')
        else:
            valid_features.append(col_name)
    if len(valid_features) == 0:
        raise ValueError(
            'The dataset does not contain any valid feature columns. ' +
            'Accepted feature types are ' + str(valid_feature_types) + '.')
    return valid_features