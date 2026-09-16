def get_layer_timing_signal_learned_1d(channels, layer, num_layers):
    shape = [num_layers, 1, 1, channels]
    layer_embedding = tf.get_variable('layer_embedding', shape, initializer
        =tf.random_normal_initializer(0, channels ** -0.5)) * channels ** 0.5
    return layer_embedding[(layer), :, :, :]