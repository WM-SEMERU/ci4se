def softmax_average_pooling_class_label_top(body_output, targets,
    model_hparams, vocab_size):
    del targets
    with tf.variable_scope(
        'softmax_average_pooling_onehot_class_label_modality_%d_%d' % (
        vocab_size, model_hparams.hidden_size)):
        x = body_output
        x = tf.reduce_mean(x, axis=1, keepdims=True)
        return tf.layers.dense(x, vocab_size)