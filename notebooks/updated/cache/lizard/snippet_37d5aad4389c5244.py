def fetch_movielens(data_home=None, indicator_features=True, genre_features
    =False, min_rating=0.0, download_if_missing=True):
    if not (indicator_features or genre_features):
        raise ValueError(
            'At least one of item_indicator_features or genre_features must be True'
            )
    zip_path = _common.get_data(data_home,
        'https://github.com/maciejkula/lightfm_datasets/releases/download/v0.1.0/movielens.zip'
        , 'movielens100k', 'movielens.zip', download_if_missing)
    try:
        train_raw, test_raw, item_metadata_raw, genres_raw = _read_raw_data(
            zip_path)
    except zipfile.BadZipFile:
        os.unlink(zip_path)
        raise ValueError(
            'Corrupted Movielens download. Check your internet connection and try again.'
            )
    num_users, num_items = _get_dimensions(_parse(train_raw), _parse(test_raw))
    train = _build_interaction_matrix(num_users, num_items, _parse(
        train_raw), min_rating)
    test = _build_interaction_matrix(num_users, num_items, _parse(test_raw),
        min_rating)
    assert train.shape == test.shape
    (id_features, id_feature_labels, genre_features_matrix,
        genre_feature_labels) = _parse_item_metadata(num_items,
        item_metadata_raw, genres_raw)
    assert id_features.shape == (num_items, len(id_feature_labels))
    assert genre_features_matrix.shape == (num_items, len(genre_feature_labels)
        )
    if indicator_features and not genre_features:
        features = id_features
        feature_labels = id_feature_labels
    elif genre_features and not indicator_features:
        features = genre_features_matrix
        feature_labels = genre_feature_labels
    else:
        features = sp.hstack([id_features, genre_features_matrix]).tocsr()
        feature_labels = np.concatenate((id_feature_labels,
            genre_feature_labels))
    data = {'train': train, 'test': test, 'item_features': features,
        'item_feature_labels': feature_labels, 'item_labels': id_feature_labels
        }
    return data