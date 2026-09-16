def blocks(self, *args, **kwargs):
    return Stream(blocks(iter(self), *args, **kwargs))