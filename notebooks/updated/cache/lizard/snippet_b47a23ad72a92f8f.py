def should_skip(app, what, name, obj, skip, options):
    if name in ['__doc__', '__module__', '__dict__', '__weakref__',
        '__abstractmethods__'] or name.startswith('_abc_'):
        return True
    return False