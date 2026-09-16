def return_reply(*types, **options):
    major = options.pop('major', DEFAULT_KATCP_MAJOR)
    if len(options) > 0:
        raise TypeError(
            'return_reply does not take keyword argument(s) %r.' % options.
            keys())
    if len(types) > 1:
        for type_ in types[:-1]:
            if type_._multiple:
                raise TypeError(
                    'Only the last parameter type can accept multiple arguments.'
                    )

    def decorator(handler):
        if not handler.__name__.startswith('request_'):
            raise ValueError(
                "This decorator can only be used on a katcp request handler (method name should start with 'request_')."
                )
        msgname = convert_method_name('request_', handler.__name__)

        @wraps(handler)
        def raw_handler(self, *args):
            reply_args = handler(self, *args)
            if gen.is_future(reply_args):
                return async_make_reply(msgname, types, reply_args, major)
            else:
                return make_reply(msgname, types, reply_args, major)
        if not getattr(handler, '_request_decorated', False):
            raw_handler._orig_argnames = inspect.getargspec(handler)[0]
        return raw_handler
    return decorator