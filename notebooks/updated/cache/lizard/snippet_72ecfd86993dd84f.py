def imagetransformer_base_8l_8h_big_cond_dr03_dan():
    hparams = imagetransformer_sep_channels_8l()
    hparams.block_width = 256
    hparams.block_length = 256
    hparams.hidden_size = 512
    hparams.num_heads = 8
    hparams.filter_size = 2048
    hparams.batch_size = 4
    hparams.max_length = 3075
    hparams.layer_preprocess_sequence = 'none'
    hparams.layer_postprocess_sequence = 'dan'
    hparams.num_decoder_layers = 8
    hparams.layer_prepostprocess_dropout = 0.3
    return hparams