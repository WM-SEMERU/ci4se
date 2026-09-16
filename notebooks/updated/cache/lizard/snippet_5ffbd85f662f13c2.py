def data_mnist(datadir=tempfile.gettempdir(), train_start=0, train_end=
    60000, test_start=0, test_end=10000):
    assert isinstance(train_start, int)
    assert isinstance(train_end, int)
    assert isinstance(test_start, int)
    assert isinstance(test_end, int)
    X_train = download_and_parse_mnist_file('train-images-idx3-ubyte.gz',
        datadir=datadir) / 255.0
    Y_train = download_and_parse_mnist_file('train-labels-idx1-ubyte.gz',
        datadir=datadir)
    X_test = download_and_parse_mnist_file('t10k-images-idx3-ubyte.gz',
        datadir=datadir) / 255.0
    Y_test = download_and_parse_mnist_file('t10k-labels-idx1-ubyte.gz',
        datadir=datadir)
    X_train = np.expand_dims(X_train, -1)
    X_test = np.expand_dims(X_test, -1)
    X_train = X_train[train_start:train_end]
    Y_train = Y_train[train_start:train_end]
    X_test = X_test[test_start:test_end]
    Y_test = Y_test[test_start:test_end]
    Y_train = utils.to_categorical(Y_train, nb_classes=10)
    Y_test = utils.to_categorical(Y_test, nb_classes=10)
    return X_train, Y_train, X_test, Y_test