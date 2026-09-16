def get(cls, service, config=None, persistence_kwargs=None, **context):
    rl_config = cls.get_config(service, config)
    context.update(service=service)
    if isinstance(rl_config, (dict, Mapping)):
        if persistence_kwargs is not None:
            rl_config.update(persistence_kwargs=persistence_kwargs)
        return RateLimiter(context, **rl_config)
    else:

        def _rl(conf):
            conf.setdefault('persistence_kwargs', persistence_kwargs or {})
            return RateLimiter(context, **conf)
        return MultiRateLimiter([_rl(config) for config in rl_config])