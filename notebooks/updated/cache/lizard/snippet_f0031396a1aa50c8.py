def adafactor_decay_rate_adam(beta2):
    t = tf.to_float(tf.train.get_or_create_global_step()) + 1.0
    decay = beta2 * (1.0 - tf.pow(beta2, t - 1.0)) / (1.0 - tf.pow(beta2, t))
    return decay