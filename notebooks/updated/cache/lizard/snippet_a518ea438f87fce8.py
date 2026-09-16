def Then2(self, f, arg1, *args, **kwargs):
    args = (arg1,) + args
    return self.ThenAt(2, f, *args, **kwargs)