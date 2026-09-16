def aggregate_single_gradient(grad_and_vars, use_mean, check_inf_nan):
    grads = [g for g, _ in grad_and_vars]
    grad = tf.add_n(grads)
    if use_mean and len(grads) > 1:
        grad = tf.multiply(grad, 1.0 / len(grads))
    v = grad_and_vars[0][1]
    if check_inf_nan:
        has_nan_or_inf = tf.logical_not(tf.reduce_all(tf.is_finite(grads)))
        return (grad, v), has_nan_or_inf
    else:
        return (grad, v), None