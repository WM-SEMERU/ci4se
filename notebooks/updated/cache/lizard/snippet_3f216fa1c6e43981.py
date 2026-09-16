def message_with_options(self, *, args=None, kwargs=None, **options):
    for name in ['on_failure', 'on_success']:
        callback = options.get(name)
        if isinstance(callback, Actor):
            options[name] = callback.actor_name
        elif not isinstance(callback, (type(None), str)):
            raise TypeError(name + ' value must be an Actor')
    return Message(queue_name=self.queue_name, actor_name=self.actor_name,
        args=args or (), kwargs=kwargs or {}, options=options)