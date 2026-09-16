def to_real_keras_layer(layer):
    from keras import layers
    if is_layer(layer, 'Dense'):
        return layers.Dense(layer.units, input_shape=(layer.input_units,))
    if is_layer(layer, 'Conv'):
        return layers.Conv2D(layer.filters, layer.kernel_size, input_shape=
            layer.input.shape, padding='same')
    if is_layer(layer, 'Pooling'):
        return layers.MaxPool2D(2)
    if is_layer(layer, 'BatchNormalization'):
        return layers.BatchNormalization(input_shape=layer.input.shape)
    if is_layer(layer, 'Concatenate'):
        return layers.Concatenate()
    if is_layer(layer, 'Add'):
        return layers.Add()
    if is_layer(layer, 'Dropout'):
        return keras_dropout(layer, layer.rate)
    if is_layer(layer, 'ReLU'):
        return layers.Activation('relu')
    if is_layer(layer, 'Softmax'):
        return layers.Activation('softmax')
    if is_layer(layer, 'Flatten'):
        return layers.Flatten()
    if is_layer(layer, 'GlobalAveragePooling'):
        return layers.GlobalAveragePooling2D()