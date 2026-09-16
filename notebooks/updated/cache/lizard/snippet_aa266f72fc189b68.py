def sepconv_relu_sepconv(inputs, filter_size, output_size,
    first_kernel_size=(1, 1), second_kernel_size=(1, 1), padding='LEFT',
    nonpadding_mask=None, dropout=0.0, name=None):
    with tf.variable_scope(name, 'sepconv_relu_sepconv', [inputs]):
        inputs = maybe_zero_out_padding(inputs, first_kernel_size,
            nonpadding_mask)
        if inputs.get_shape().ndims == 3:
            is_3d = True
            inputs = tf.expand_dims(inputs, 2)
        else:
            is_3d = False
        h = separable_conv(inputs, filter_size, first_kernel_size,
            activation=tf.nn.relu, padding=padding, name='conv1')
        if dropout != 0.0:
            h = tf.nn.dropout(h, 1.0 - dropout)
        h = maybe_zero_out_padding(h, second_kernel_size, nonpadding_mask)
        ret = separable_conv(h, output_size, second_kernel_size, padding=
            padding, name='conv2')
        if is_3d:
            ret = tf.squeeze(ret, 2)
        return ret