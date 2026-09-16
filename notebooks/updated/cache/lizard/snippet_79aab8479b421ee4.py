def _get_bakery_dynamic_attr(self, attname, obj, args=None, default=None):
    try:
        attr = getattr(self, attname)
    except AttributeError:
        return default
    if callable(attr) or args:
        args = args[:] if args else []
        try:
            code = six.get_function_code(attr)
        except AttributeError:
            code = six.get_function_code(attr.__call__)
        if code.co_argcount == 2 + len(args):
            args.append(obj)
        return attr(*args)
    return attr