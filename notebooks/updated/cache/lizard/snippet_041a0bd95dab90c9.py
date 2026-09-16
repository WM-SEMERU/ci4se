def actor(fn=None, *, actor_class=Actor, actor_name=None, queue_name=
    'default', priority=0, broker=None, **options):

    def decorator(fn):
        nonlocal actor_name, broker
        actor_name = actor_name or fn.__name__
        if not _queue_name_re.fullmatch(queue_name):
            raise ValueError(
                'Queue names must start with a letter or an underscore followed by any number of letters, digits, dashes or underscores.'
                )
        broker = broker or get_broker()
        invalid_options = set(options) - broker.actor_options
        if invalid_options:
            invalid_options_list = ', '.join(invalid_options)
            raise ValueError(
                'The following actor options are undefined: %s. Did you forget to add a middleware to your Broker?'
                 % invalid_options_list)
        return actor_class(fn, actor_name=actor_name, queue_name=queue_name,
            priority=priority, broker=broker, options=options)
    if fn is None:
        return decorator
    return decorator(fn)