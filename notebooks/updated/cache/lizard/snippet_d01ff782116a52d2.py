def options(self, *args, **kwargs):
    return self.session.options(*args, **self.get_kwargs(**kwargs))