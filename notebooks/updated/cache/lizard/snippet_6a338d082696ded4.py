def get_nn_classifier(X, y):
    assert type(X) is numpy.ndarray
    assert type(y) is numpy.ndarray
    assert len(X) == len(y)
    assert X.dtype == 'float32'
    assert y.dtype == 'int32'
    nn_pickled_filename = 'is_one_symbol_classifier.pickle'
    if os.path.isfile(nn_pickled_filename):
        with open(nn_pickled_filename, 'rb') as handle:
            get_output = pickle.load(handle)
    else:
        get_output = train_nn_segmentation_classifier(X, y)
        with open(nn_pickled_filename, 'wb') as handle:
            pickle.dump(get_output, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return get_output