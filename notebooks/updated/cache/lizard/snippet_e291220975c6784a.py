def _with_context(self, *args, **kwargs):
    context = dict(args[0] if args else self.env.context, **kwargs)
    return self.with_env(self.env(context=context))