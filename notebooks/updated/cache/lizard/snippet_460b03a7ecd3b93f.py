def option(func, *args, **attrs):
    if click is None:
        return func

    def decorator(f):
        name = attrs.pop('name', func.__name__.replace('_', '-'))
        attrs.setdefault('help', func.__doc__)
        attrs.setdefault('required', False)
        if not attrs.get('is_flag'):
            attrs.setdefault('show_default', True)
            attrs.setdefault('metavar', name.replace('-', '_').upper())
            attrs.setdefault('type', str)
        if not name.startswith('-'):
            name = '--%s' % name
        return click.option(name, *args, **attrs)(f)
    return decorator