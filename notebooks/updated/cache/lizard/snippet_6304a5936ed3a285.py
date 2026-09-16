def shift(self, *args, **kwargs):
    for item in self:
        item.shift(*args, **kwargs)