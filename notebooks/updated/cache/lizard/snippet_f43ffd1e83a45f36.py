def is_inbound_presence_filter(cb):
    try:
        handlers = get_magic_attr(cb)
    except AttributeError:
        return False
    hs = HandlerSpec((_apply_inbound_presence_filter, ()))
    return hs in handlers