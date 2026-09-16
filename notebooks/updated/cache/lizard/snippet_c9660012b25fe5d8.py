def debug(self, msg, *args, **kwargs):
    kwargs.setdefault('inc_stackinfo', True)
    self.log(DEBUG, msg, args, **kwargs)