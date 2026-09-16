def imagetransformer_base_10l_8h_big_uncond_dr03_dan_64():
    hparams = imagetransformer_base_10l_8h_big_cond_dr03_dan()
    hparams.unconditional = True
    hparams.max_length = 14000
    hparams.batch_size = 1
    hparams.img_len = 64
    hparams.layer_prepostprocess_dropout = 0.1
    return hparams