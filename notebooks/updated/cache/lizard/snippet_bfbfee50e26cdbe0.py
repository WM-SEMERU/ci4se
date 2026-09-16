def attrsignal(descriptor, signal_name, *, defer=False):

    def decorator(f):
        add_handler_spec(f, _attrsignal_spec(descriptor, signal_name, f, defer)
            )
        return f
    return decorator