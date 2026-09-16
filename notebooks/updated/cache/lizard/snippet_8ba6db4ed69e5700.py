def command_err(self, code=1, errmsg='MockupDB command failure', *args, **
    kwargs):
    kwargs.setdefault('ok', 0)
    kwargs['code'] = code
    kwargs['errmsg'] = errmsg
    self.replies(*args, **kwargs)
    return True