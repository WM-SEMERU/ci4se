def setup_model(x, y, model_type='random_forest', seed=None, **kwargs):
    assert len(x) > 1 and len(y
        ) > 1, 'Not enough data objects to train on (minimum is at least two, you have (x: {0}) and (y: {1}))'.format(
        len(x), len(y))
    sets = namedtuple('Datasets', ['train', 'test'])
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=
        seed, shuffle=False)
    x = sets(x_train, x_test)
    y = sets(y_train, y_test)
    if model_type == 'random_forest' or model_type == 'rf':
        model = rf.RandomForest(x, y, random_state=seed, **kwargs)
    elif model_type == 'deep_neural_network' or model_type == 'dnn':
        model = dnn.DeepNeuralNetwork(x, y, **kwargs)
    else:
        raise ValueError('Invalid model type kwarg')
    return model