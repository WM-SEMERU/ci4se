def add_done_callback(self, function, **kwargs):
    with self._callbacks_lock:
        _function = functools.partial(function, **kwargs)
        self._done_callbacks.append(_function)