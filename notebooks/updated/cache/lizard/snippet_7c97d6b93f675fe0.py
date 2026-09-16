def put(self, path, value, timeout=None, event_timeout=None):
    future = self.put_async(path, value)
    self.wait_all_futures(future, timeout=timeout, event_timeout=event_timeout)
    return future.result()