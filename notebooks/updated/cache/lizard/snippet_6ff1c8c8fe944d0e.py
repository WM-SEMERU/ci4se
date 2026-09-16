def sinkhorn(inputs, n_iters=20):
    vocab_size = tf.shape(inputs)[-1]
    log_alpha = tf.reshape(inputs, [-1, vocab_size, vocab_size])
    for _ in range(n_iters):
        log_alpha -= tf.reshape(tf.reduce_logsumexp(log_alpha, axis=2), [-1,
            vocab_size, 1])
        log_alpha -= tf.reshape(tf.reduce_logsumexp(log_alpha, axis=1), [-1,
            1, vocab_size])
    outputs = tf.exp(log_alpha)
    return outputs