def revnet_base():
    hparams = common_hparams.basic_params1()
    hparams.add_hparam('num_channels', [64, 128, 256, 416])
    hparams.add_hparam('num_layers_per_block', [1, 1, 10, 1])
    hparams.add_hparam('bottleneck', True)
    hparams.add_hparam('first_batch_norm', [False, True, True, True])
    hparams.add_hparam('init_stride', 2)
    hparams.add_hparam('init_kernel_size', 7)
    hparams.add_hparam('init_maxpool', True)
    hparams.add_hparam('strides', [1, 2, 2, 2])
    hparams.add_hparam('num_channels_init_block', 64)
    hparams.add_hparam('dim', '2d')
    hparams.initializer = 'normal_unit_scaling'
    hparams.initializer_gain = 2.0
    hparams.optimizer = 'Momentum'
    hparams.optimizer_momentum_momentum = 0.9
    hparams.optimizer_momentum_nesterov = True
    hparams.weight_decay = 0.0001
    hparams.clip_grad_norm = 0.0
    hparams.learning_rate = 0.4
    hparams.learning_rate_decay_scheme = 'cosine'
    hparams.learning_rate_cosine_cycle_steps = 120000
    hparams.batch_size = 128
    return hparams