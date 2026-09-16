def bytenet_base():
    hparams = common_hparams.basic_params1()
    hparams.batch_size = 2048
    hparams.hidden_size = 768
    hparams.dropout = 0.2
    hparams.symbol_dropout = 0.2
    hparams.label_smoothing = 0.1
    hparams.clip_grad_norm = 2.0
    hparams.num_hidden_layers = 4
    hparams.kernel_height = 3
    hparams.kernel_width = 1
    hparams.learning_rate_decay_scheme = 'exp'
    hparams.learning_rate = 0.05
    hparams.learning_rate_warmup_steps = 3000
    hparams.initializer_gain = 1.0
    hparams.weight_decay = 3.0
    hparams.num_sampled_classes = 0
    hparams.sampling_method = 'argmax'
    hparams.optimizer_adam_epsilon = 1e-06
    hparams.optimizer_adam_beta1 = 0.85
    hparams.optimizer_adam_beta2 = 0.997
    hparams.add_hparam('num_block_repeat', 4)
    return hparams