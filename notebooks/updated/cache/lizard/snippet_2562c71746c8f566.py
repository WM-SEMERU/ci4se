def actnorm_3d(name, x, logscale_factor=3.0):
    with tf.variable_scope(name, reuse=tf.AUTO_REUSE):
        x = tf.unstack(x, axis=1)
        x_normed = []
        for ind, x_step in enumerate(x):
            x_step, _ = actnorm('actnorm_%d' % ind, x_step, logscale_factor
                =logscale_factor)
            x_normed.append(x_step)
        return tf.stack(x_normed, axis=1), None