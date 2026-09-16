def encdec_attention_1d(x, encoder_output, encoder_decoder_attention_bias,
    hparams):
    x, x_shape, is_4d = maybe_reshape_4d_to_3d(x)
    encoder_output, _, _ = maybe_reshape_4d_to_3d(encoder_output)
    with tf.variable_scope('encdec_attention'):
        y = common_attention.multihead_attention(x, encoder_output,
            encoder_decoder_attention_bias, hparams.attention_key_channels or
            hparams.hidden_size, hparams.attention_value_channels or
            hparams.hidden_size, hparams.hidden_size, hparams.num_heads,
            hparams.attention_dropout, name='encdec_attention')
    if is_4d:
        y = tf.reshape(y, x_shape)
        y.set_shape([None, None, None, hparams.hidden_size])
    return y