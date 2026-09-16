def unit(x1, x2, block_num, depth, num_layers, dim='2d', bottleneck=True,
    first_batch_norm=True, stride=1, training=True):
    scope_name = 'unit_%d' % block_num
    if bottleneck:
        depth1 = depth
        depth2 = depth * 4
    else:
        depth1 = depth2 = depth
    residual = wrapped_partial(f, depth1=depth1, depth2=depth2, dim=dim,
        training=training, bottleneck=bottleneck)
    with tf.variable_scope(scope_name):
        downsample = (downsample_bottleneck if bottleneck else
            downsample_residual)
        with tf.variable_scope('downsampling'):
            with tf.variable_scope('x1'):
                hx1 = downsample(x1, depth2, dim=dim, stride=stride)
                fx2 = residual(x2, stride=stride, first_batch_norm=
                    first_batch_norm)
                x1 = hx1 + fx2
            with tf.variable_scope('x2'):
                hx2 = downsample(x2, depth2, dim=dim, stride=stride)
                fx1 = residual(x1)
                x2 = hx2 + fx1
        with tf.variable_scope('full_block'):
            x1, x2 = tf.contrib.layers.rev_block(x1, x2, residual, residual,
                num_layers=num_layers)
            return x1, x2