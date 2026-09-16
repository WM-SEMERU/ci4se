def imagetransformer_b12l_4h_b128_h512_uncond_dr01_im():
    hparams = imagetransformer_b12l_4h_b256_uncond_dr03_tpu()
    update_hparams_for_tpu(hparams)
    hparams.batch_size = 4
    hparams.optimizer = 'Adafactor'
    hparams.learning_rate_schedule = 'rsqrt_decay'
    hparams.learning_rate_warmup_steps = 6000
    hparams.layer_prepostprocess_dropout = 0.1
    return hparams