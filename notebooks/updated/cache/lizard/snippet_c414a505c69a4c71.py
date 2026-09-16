def init(**kw):
    if getattr(__local, '__context', None):
        raise ValueError('fedmsg already initialized')
    config = fedmsg.config.load_config([], None)
    config.update(kw)
    __local.__context = fedmsg.core.FedMsgContext(**config)
    return __local.__context