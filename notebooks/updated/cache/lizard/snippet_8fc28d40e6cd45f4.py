def get_message_from_call(self, *args, **kwargs):
    if len(args) == 1 and isinstance(args[0], dict):
        self.logger.debug('called with arg dictionary')
        result = args[0]
    elif len(args) == 0 and kwargs != {}:
        self.logger.debug('called with kwargs')
        result = kwargs
    else:
        self.logger.error('get_message_from_call could not handle "%r", "%r"',
            args, kwargs)
        raise TypeError(
            'Pass either keyword arguments or a dictionary argument')
    return self.message_class(result)