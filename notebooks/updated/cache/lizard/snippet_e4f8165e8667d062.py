def _onmessage(cls, kmsg):
    logger.debug('{}.ReceivedMessage {}[{}]'.format(cls.__name__, kmsg.
        entrypoint, kmsg.uuid), extra=dict(kmsg=kmsg.dump()))
    return cls.onmessage(kmsg)