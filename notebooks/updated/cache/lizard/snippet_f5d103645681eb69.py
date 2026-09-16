def l2_regression_loss(y, target, name=None):
    with tf.name_scope(name, 'l2_regression', [y, target]) as scope:
        y = tf.convert_to_tensor(y, name='y')
        target = tf.convert_to_tensor(target, name='target')
        return tf.sqrt(l2_regression_sq_loss(y, target, name=scope))