def single_discriminator(x, filters=128, kernel_size=8, strides=4,
    pure_mean=False):
    with tf.variable_scope('discriminator'):
        net = layers().Conv2D(filters, kernel_size, strides=strides,
            padding='SAME', name='conv1')(x)
        if pure_mean:
            net = tf.reduce_mean(net, [1, 2])
        else:
            net = mean_with_attention(net, 'mean_with_attention')
        return net