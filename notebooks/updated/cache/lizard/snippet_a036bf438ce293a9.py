def cppn(width, batch=1, num_output_channels=3, num_hidden_channels=24,
    num_layers=8, activation_func=_composite_activation, normalize=False):
    r = 3.0 ** 0.5
    coord_range = tf.linspace(-r, r, width)
    y, x = tf.meshgrid(coord_range, coord_range, indexing='ij')
    net = tf.stack([tf.stack([x, y], -1)] * batch, 0)
    with slim.arg_scope([slim.conv2d], kernel_size=[1, 1], activation_fn=
        None, weights_initializer=tf.initializers.variance_scaling(),
        biases_initializer=tf.initializers.random_normal(0.0, 0.1)):
        for i in range(num_layers):
            x = slim.conv2d(net, num_hidden_channels)
            if normalize:
                x = slim.instance_norm(x)
            net = activation_func(x)
        rgb = slim.conv2d(net, num_output_channels, activation_fn=tf.nn.
            sigmoid, weights_initializer=tf.zeros_initializer())
    return rgb