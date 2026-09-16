def image_channel_compress_top(body_output, targets, model_hparams, vocab_size
    ):
    del targets
    with tf.variable_scope('image_channel_compress_modality'):
        hidden_size = model_hparams.hidden_size
        img_len = model_hparams.img_len
        channels = 3
        batch = common_layers.shape_list(body_output)[0]
        x = tf.layers.conv2d(body_output, hidden_size * channels,
            kernel_size=(1, 1), strides=(1, 1), padding='VALID', activation
            =tf.nn.relu, name='decompress_conv')
        x = tf.reshape(x, [batch, img_len, img_len * channels, hidden_size])
        x = common_layers.layer_preprocess(x, model_hparams)
        x = tf.layers.dense(x, vocab_size, use_bias=True, activation=None,
            name='output_conv')
        x = tf.reshape(x, [batch, img_len, img_len, channels, vocab_size])
        return x