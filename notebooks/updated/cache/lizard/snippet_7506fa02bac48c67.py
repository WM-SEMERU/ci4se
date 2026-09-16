def patch_discriminator(x, filters=64, filter_size=5, n=4, name='patch_discrim'
    ):
    with tf.variable_scope(name):
        x_shape = shape_list(x)
        spatial_dims = [x_shape[1] // 4, x_shape[2] // 4]
        x = tf.random_crop(x, [x_shape[0]] + spatial_dims + [x_shape[3]])
        for i in range(n):
            x = general_conv(x=x, num_filters=filters * 2 ** i, filter_size
                =filter_size, stride=2 if i != n - 1 else 1, stddev=0.02,
                padding='SAME', name='c%d' % i, do_norm='instance' if i != 
                0 else False, do_relu=i != n - 1, relufactor=0.2)
        x = tf.reduce_mean(x, [1, 2])
        return x