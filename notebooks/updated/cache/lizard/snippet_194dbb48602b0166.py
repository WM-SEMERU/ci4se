def submit_future(self, func, *args, **kwargs):
    if self.config['sync_http'] is True:
        return MockFuture(func, *args, **kwargs)
    future = self.pool.submit(func, *args, **kwargs)
    self.futures.append(future)
    return future