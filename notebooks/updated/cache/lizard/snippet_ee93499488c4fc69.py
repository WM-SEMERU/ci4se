def conv_lstm_2d(inputs, state, output_channels, kernel_size=5, name=None,
    spatial_dims=None):
    input_shape = common_layers.shape_list(inputs)
    batch_size, input_channels = input_shape[0], input_shape[-1]
    if spatial_dims is None:
        input_shape = input_shape[1:]
    else:
        input_shape = spatial_dims + [input_channels]
    cell = tf.contrib.rnn.ConvLSTMCell(2, input_shape, output_channels, [
        kernel_size, kernel_size], name=name)
    if state is None:
        state = cell.zero_state(batch_size, tf.float32)
    outputs, new_state = cell(inputs, state)
    return outputs, new_state