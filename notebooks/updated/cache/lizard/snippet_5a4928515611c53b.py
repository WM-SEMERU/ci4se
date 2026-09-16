def add_step_timing_signal(x, step, hparams):
    if hparams.recurrence_type == 'act':
        num_steps = hparams.act_max_steps
    else:
        num_steps = hparams.num_rec_steps
    channels = common_layers.shape_list(x)[-1]
    if hparams.step_timing_signal_type == 'learned':
        signal = common_attention.get_layer_timing_signal_learned_1d(channels,
            step, num_steps)
    elif hparams.step_timing_signal_type == 'sinusoid':
        signal = common_attention.get_layer_timing_signal_sinusoid_1d(channels,
            step, num_steps)
    if hparams.add_or_concat_timing_signal == 'add':
        x_with_timing = x + common_layers.cast_like(signal, x)
    elif hparams.add_or_concat_timing_signal == 'concat':
        batch_size = common_layers.shape_list(x)[0]
        length = common_layers.shape_list(x)[1]
        signal_tiled = tf.tile(signal, [batch_size, length, 1])
        x_with_timing = tf.concat((x, signal_tiled), axis=-1)
    return x_with_timing