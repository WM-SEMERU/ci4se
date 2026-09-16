def sequence_accuracy(labels, outputs):
    all_correct = tf.reduce_all(tf.logical_or(tf.equal(labels, outputs), tf
        .equal(labels, 0)), axis=-1)
    return tf.metrics.mean(all_correct)