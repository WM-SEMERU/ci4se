def run_task(func):

    def _wrapped(*a, **k):
        gen = func(*a, **k)
        return _consume_task(gen)
    return _wrapped