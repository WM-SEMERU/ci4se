def start(self, *args, **kwargs):
    wait = kwargs.pop('wait', False)
    self._setup(*args, **kwargs)
    self.build(*args, **kwargs)
    self.submit_tasks(wait=wait)