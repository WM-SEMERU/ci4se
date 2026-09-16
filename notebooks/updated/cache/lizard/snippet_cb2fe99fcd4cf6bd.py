def mtf_transformer_lm_baseline():
    hparams = mtf_transformer_paper_lm(-1)
    hparams.batch_size = 128
    hparams.learning_rate_decay_steps = 27200
    hparams.mesh_shape = 'batch:8'
    return hparams