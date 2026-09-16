def render(filepath, context=None, **options):
    if filepath == '-':
        return _render(sys.stdin.read(), context=context, **options)
    return _render(filepath=filepath, context=context, **options)