def auto_update_attrs_from_kwargs(method):

    def wrapped(self, **kwargs):
        argspec = inspect.getargspec(method)
        defaults = argspec.defaults or ()
        nb_args, nb_defaults = len(argspec.args), len(defaults)
        options = dict(zip(argspec.args[nb_args - nb_defaults:], defaults))
        options.update(kwargs)
        self.__dict__.update(options)
        method(self, **kwargs)
    return wrapped