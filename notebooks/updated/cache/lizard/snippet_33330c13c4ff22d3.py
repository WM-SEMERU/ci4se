def create_output(decoder_output, rows, cols, targets, hparams):
    del targets
    decoded_image = postprocess_image(decoder_output, rows, cols, hparams)
    batch = common_layers.shape_list(decoded_image)[0]
    depth = common_layers.shape_list(decoded_image)[-1]
    likelihood = getattr(hparams, 'likelihood', DistributionType.CAT)
    if hparams.mode == tf.estimator.ModeKeys.PREDICT:
        y = tf.reshape(decoded_image, [batch, -1, 1, 1, depth])
        output = y[:, :rows, :, :, :]
    elif likelihood == DistributionType.CAT:
        channels = hparams.num_channels
        output = tf.reshape(decoded_image, [batch, rows, cols // channels,
            channels, depth])
    else:
        output = decoded_image
    return output