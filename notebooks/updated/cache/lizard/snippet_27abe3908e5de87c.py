def experimental(message):

    def f__(f):

        def f_(*args, **kwargs):
            from warnings import warn
            warn(message, category=ExperimentalWarning, stacklevel=2)
            return f(*args, **kwargs)
        f_.__name__ = f.__name__
        f_.__doc__ = f.__doc__
        f_.__dict__.update(f.__dict__)
        return f_
    return f__