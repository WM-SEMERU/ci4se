def sg_regularizer_loss(scale=1.0):
    r
    return scale * tf.reduce_mean(tf.get_collection(tf.GraphKeys.
        REGULARIZATION_LOSSES))