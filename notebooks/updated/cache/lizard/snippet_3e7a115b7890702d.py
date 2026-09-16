def compress_encoder_1d(x, hparams, name=None):
    x = tf.expand_dims(x, axis=2)
    return compress_encoder(x, hparams, strides=(2, 1), kernel_size=(
        hparams.kernel_size, 1), name=name)