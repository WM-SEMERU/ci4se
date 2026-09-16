def adafactor_optimizer_from_hparams(hparams, lr):
    if hparams.optimizer_adafactor_decay_type == 'Adam':
        decay_rate = adafactor_decay_rate_adam(hparams.
            optimizer_adafactor_beta2)
    elif hparams.optimizer_adafactor_decay_type == 'pow':
        decay_rate = adafactor_decay_rate_pow(hparams.
            optimizer_adafactor_memory_exponent)
    else:
        raise ValueError('unknown optimizer_adafactor_decay_type')
    return AdafactorOptimizer(multiply_by_parameter_scale=hparams.
        optimizer_adafactor_multiply_by_parameter_scale, learning_rate=lr,
        decay_rate=decay_rate, beta1=hparams.optimizer_adafactor_beta1,
        clipping_threshold=hparams.optimizer_adafactor_clipping_threshold,
        factored=hparams.optimizer_adafactor_factored)