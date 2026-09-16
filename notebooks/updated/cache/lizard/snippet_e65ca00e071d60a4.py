def inject():
    try:
        from .compat import builtins
        module = sys.modules[__name__]
        setattr(builtins, __name__, module)
    except ImportError:
        pass