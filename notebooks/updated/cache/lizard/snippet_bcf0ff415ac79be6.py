def decode_to_shape(inputs, shape, scope):
    with tf.variable_scope(scope, reuse=tf.AUTO_REUSE):
        x = inputs
        x = tfl.flatten(x)
        x = tfl.dense(x, shape[2], activation=None, name='dec_dense')
        x = tf.expand_dims(x, axis=1)
        return x