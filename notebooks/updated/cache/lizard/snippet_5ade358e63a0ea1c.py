def require_pip_module(module):

    def wrapper(func, *args, **kwargs):
        try:
            __import__(module)
        except ImportError:
            sys.stderr.write('`pip install %s` to enable this feature\n' %
                module)
            sys.exit(1)
        else:
            return func(*args, **kwargs)
    return decorator(wrapper)