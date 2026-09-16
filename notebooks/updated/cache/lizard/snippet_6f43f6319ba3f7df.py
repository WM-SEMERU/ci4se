def err_write(self, msg, **kwargs):
    r
    if self._thread_invalid():
        self.async_call(self.err_write, msg, **kwargs)
        return
    return self.request('nvim_err_write', msg, **kwargs)