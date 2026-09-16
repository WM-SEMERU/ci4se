def skip_status(*skipped):

    def decorator(func):

        @functools.wraps(func)
        def _skip_status(self, *args, **kwargs):
            if self.status not in skipped:
                return func(self, *args, **kwargs)
        return _skip_status
    return decorator