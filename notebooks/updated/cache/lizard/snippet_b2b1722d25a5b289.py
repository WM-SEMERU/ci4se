def pad_conv3d_lrelu(self, activations, n_filters, kernel_size, strides, scope
    ):
    padding = [[0, 0], [1, 1], [1, 1], [1, 1], [0, 0]]
    if isinstance(strides, numbers.Integral):
        strides = [strides] * 3
    strides = [1] + strides + [1]
    filter_shape = [kernel_size] * 3 + activations.shape[-1:].as_list() + [
        n_filters]
    with tf.variable_scope(scope, reuse=tf.AUTO_REUSE):
        conv_filter = tf.get_variable('conv_filter', shape=filter_shape,
            initializer=tf.truncated_normal_initializer(stddev=0.02))
        if self.hparams.use_spectral_norm:
            conv_filter, assign_op = common_layers.apply_spectral_norm(
                conv_filter)
            if self.is_training:
                tf.add_to_collection(tf.GraphKeys.UPDATE_OPS, assign_op)
        padded = tf.pad(activations, padding)
        convolved = tf.nn.conv3d(padded, conv_filter, strides=strides,
            padding='VALID')
        rectified = tf.nn.leaky_relu(convolved, alpha=0.2)
    return rectified