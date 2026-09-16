def is_builtin(text):
    from spyder.py3compat import builtins
    return text in [str(name) for name in dir(builtins) if not name.
        startswith('_')]