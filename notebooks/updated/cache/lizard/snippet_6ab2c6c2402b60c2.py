def all(self, timeout=None, max_concurrency=64, auto_batch=True):
    return self.fanout('all', timeout=timeout, max_concurrency=
        max_concurrency, auto_batch=auto_batch)