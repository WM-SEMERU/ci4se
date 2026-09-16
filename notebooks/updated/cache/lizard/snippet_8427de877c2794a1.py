def transformer_tall_pretrain_lm_tpu_adafactor():
    hparams = transformer_tall_pretrain_lm()
    update_hparams_for_tpu(hparams)
    hparams.max_length = 1024
    hparams.batch_size = 8
    hparams.multiproblem_vocab_size = 2 ** 16
    return hparams