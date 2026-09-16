def publish(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        payload = func(self, *args, **kwargs)
        payload.pop('self', None)
        self._publish(func.__name__, payload)
        return None
    wrapper.is_publish = True
    return wrapper