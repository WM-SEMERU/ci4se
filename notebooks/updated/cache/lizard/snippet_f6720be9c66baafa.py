def maybe_wait(func):

    def wrapper(self, *args, **kwargs):
        if self.slow:
            time.sleep(random.randint(5, 15))
        return func(self, *args, **kwargs)
    return wrapper