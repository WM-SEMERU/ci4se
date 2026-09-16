def lstm_seq2seq_internal_bid_encoder(inputs, targets, hparams, train):
    with tf.variable_scope('lstm_seq2seq_bid_encoder'):
        if inputs is not None:
            inputs_length = common_layers.length_from_embedding(inputs)
            inputs = common_layers.flatten4d3d(inputs)
            _, final_encoder_state = lstm_bid_encoder(inputs, inputs_length,
                hparams, train, 'encoder')
        else:
            inputs_length = None
            final_encoder_state = None
        shifted_targets = common_layers.shift_right(targets)
        targets_length = common_layers.length_from_embedding(shifted_targets
            ) + 1
        hparams_decoder = copy.copy(hparams)
        hparams_decoder.hidden_size = 2 * hparams.hidden_size
        decoder_outputs, _ = lstm(common_layers.flatten4d3d(shifted_targets
            ), targets_length, hparams_decoder, train, 'decoder',
            initial_state=final_encoder_state)
        return tf.expand_dims(decoder_outputs, axis=2)