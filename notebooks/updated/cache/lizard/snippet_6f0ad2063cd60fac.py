def add_timing_signal_1d_given_position(x, position, min_timescale=1.0,
    max_timescale=10000.0):
    channels = common_layers.shape_list(x)[2]
    num_timescales = channels // 2
    log_timescale_increment = math.log(float(max_timescale) / float(
        min_timescale)) / (tf.to_float(num_timescales) - 1)
    inv_timescales = min_timescale * tf.exp(tf.to_float(tf.range(
        num_timescales)) * -log_timescale_increment)
    scaled_time = tf.expand_dims(tf.to_float(position), 2) * tf.expand_dims(tf
        .expand_dims(inv_timescales, 0), 0)
    signal = tf.concat([tf.sin(scaled_time), tf.cos(scaled_time)], axis=2)
    signal = tf.pad(signal, [[0, 0], [0, 0], [0, tf.mod(channels, 2)]])
    signal = common_layers.cast_like(signal, x)
    return x + signal