def with_context(cls, *args, **kwargs):
    context = dict(args[0] if args else cls.env.context, **kwargs)
    return cls.with_env(cls.env(context=context))