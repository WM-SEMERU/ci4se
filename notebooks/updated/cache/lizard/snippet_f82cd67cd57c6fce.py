def client_side(func):

    def inner(*args, **kwargs):
        if args and hasattr(args[0], 'is_server') and voltron.debugger:
            raise ClientSideOnlyException(
                'This method can only be called on a client-side instance')
        return func(*args, **kwargs)
    return inner