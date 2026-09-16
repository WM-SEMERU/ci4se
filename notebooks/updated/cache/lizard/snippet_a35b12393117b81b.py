def data_cifar10(train_start=0, train_end=50000, test_start=0, test_end=10000):
    img_rows = 32
    img_cols = 32
    nb_classes = 10
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    if tf.keras.backend.image_data_format() == 'channels_first':
        x_train = x_train.reshape(x_train.shape[0], 3, img_rows, img_cols)
        x_test = x_test.reshape(x_test.shape[0], 3, img_rows, img_cols)
    else:
        x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 3)
        x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 3)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')
    y_train = np_utils.to_categorical(y_train, nb_classes)
    y_test = np_utils.to_categorical(y_test, nb_classes)
    x_train = x_train[train_start:train_end, :, :, :]
    y_train = y_train[train_start:train_end, :]
    x_test = x_test[test_start:test_end, :]
    y_test = y_test[test_start:test_end, :]
    return x_train, y_train, x_test, y_test