def does_not_raise(self, function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except Exception as e:
        self.log_error('{} did raise {}: {}'.format(function.__name__, type
            (e).__name__, e), None)