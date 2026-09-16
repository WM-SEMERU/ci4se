def safe_call(self, kwargs, args=None):
    try:
        return self._func(**kwargs)
    except Exception as exc:
        if args and getattr(args, 'debug', False):
            raise
        return str(exc)