def prepare_question_encoder(inputs, hparams):
    encoder_input = inputs
    encoder_padding = common_attention.embedding_to_padding(encoder_input)
    ignore_padding = common_attention.attention_bias_ignore_padding(
        encoder_padding)
    encoder_self_attention_bias = ignore_padding
    if hparams.pos == 'timing':
        encoder_input = common_attention.add_timing_signal_1d(encoder_input)
    elif hparams.pos == 'emb':
        encoder_input = common_attention.add_positional_embedding(encoder_input
            , hparams.max_length, 'inputs_positional_embedding', None)
    return encoder_input, encoder_self_attention_bias