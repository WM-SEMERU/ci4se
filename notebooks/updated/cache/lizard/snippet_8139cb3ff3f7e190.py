def from_config(cls, cp, **kwargs):
    r
    args = cls._init_args_from_config(cp)
    args['low_frequency_cutoff'] = low_frequency_cutoff_from_config(cp)
    args['high_frequency_cutoff'] = high_frequency_cutoff_from_config(cp)
    ignore_args = ['name', 'low-frequency-cutoff', 'high-frequency-cutoff']
    args.update(cls.extra_args_from_config(cp, 'model', skip_args=ignore_args))
    args.update(kwargs)
    return cls(**args)