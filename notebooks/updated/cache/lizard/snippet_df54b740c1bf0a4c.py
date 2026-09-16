def next_frame_sv2p_discrete():
    hparams = next_frame_sv2p()
    hparams.action_injection = 'multiplicative'
    hparams.small_mode = True
    hparams.add_hparam('bottleneck_bits', 128)
    hparams.add_hparam('bottleneck_noise', 0.02)
    hparams.add_hparam('discrete_warmup_steps', 40000)
    hparams.add_hparam('full_latent_tower', False)
    hparams.add_hparam('latent_predictor_state_size', 128)
    hparams.add_hparam('latent_predictor_temperature', 0.5)
    hparams.add_hparam('discretize_warmup_steps', 40000)
    return hparams