def _spawn(self, func, *args, **kwargs):
    gevent.spawn(func, *args, **kwargs)