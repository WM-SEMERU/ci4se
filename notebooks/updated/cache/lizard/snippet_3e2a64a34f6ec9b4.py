def request(self, *args, **kwargs):
    func = partial(super().request, *args, **kwargs)
    return self.loop.run_in_executor(self.thread_pool, func)