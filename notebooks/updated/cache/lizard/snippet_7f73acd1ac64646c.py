def prepare_csv_to_dataframe(data_file, config, use_target=True):
    names, dtypes = [], []
    model = config.get_data_model()
    for feature in model:
        assert feature.get_name(
            ) not in names, "Two features can't have the same name."
        if not use_target and feature.is_target():
            continue
        names.append(feature.get_name())
    data = pd.read_csv(data_file, names=names)
    transform_categorical_features(config, data, use_target)
    return data