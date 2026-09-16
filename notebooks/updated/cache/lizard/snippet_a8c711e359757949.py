def readlines(self, *args, **kwargs):
    return list(iter(partial(self.readline, *args, **kwargs), ''))