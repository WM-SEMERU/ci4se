def init(images, num_channels, dim='2d', stride=2, kernel_size=7, maxpool=
    True, training=True, scope='init'):
    conv = CONFIG[dim]['conv']
    pool = CONFIG[dim]['max_pool']
    with tf.variable_scope(scope):
        net = conv(images, num_channels, kernel_size, strides=stride,
            padding='SAME', activation=None)
        net = tf.layers.batch_normalization(net, training=training)
        net = tf.nn.relu(net)
        if maxpool:
            net = pool(net, pool_size=3, strides=stride)
        x1, x2 = tf.split(net, 2, axis=CONFIG[dim]['split_axis'])
        return x1, x2