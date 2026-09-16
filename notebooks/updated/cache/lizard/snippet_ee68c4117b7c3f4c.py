def add_errback(self, fn, *args, **kwargs):
    run_now = False
    with self._callback_lock:
        self._errbacks.append((fn, args, kwargs))
        if self._final_exception:
            run_now = True
    if run_now:
        fn(self._final_exception, *args, **kwargs)
    return self