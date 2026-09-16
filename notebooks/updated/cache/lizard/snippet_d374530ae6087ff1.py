def pearson_correlation_coefficient(predictions, labels, weights_fn=None):
    del weights_fn
    _, pearson = tf.contrib.metrics.streaming_pearson_correlation(predictions,
        labels)
    return pearson, tf.constant(1.0)