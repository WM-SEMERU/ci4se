def video_top(body_output, targets, model_hparams, vocab_size):
    del targets
    num_channels = model_hparams.problem.num_channels
    shape = common_layers.shape_list(body_output)
    reshape_shape = shape[:-1] + [num_channels, vocab_size]
    res = tf.reshape(body_output, reshape_shape)
    x = tf.argmax(tf.reshape(res, [-1, vocab_size]), axis=-1)
    x = tf.reshape(x, shape[:-1] + [num_channels])
    common_video.gif_summary('results', x, max_outputs=1)
    return res