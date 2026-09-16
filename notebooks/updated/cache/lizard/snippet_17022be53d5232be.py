def autoencoder_autoregressive():
    hparams = autoencoder_basic()
    hparams.add_hparam('autoregressive_forget_base', False)
    hparams.add_hparam('autoregressive_mode', 'none')
    hparams.add_hparam('autoregressive_decode_steps', 0)
    hparams.add_hparam('autoregressive_eval_pure_autoencoder', False)
    hparams.add_hparam('autoregressive_gumbel_sample', False)
    return hparams