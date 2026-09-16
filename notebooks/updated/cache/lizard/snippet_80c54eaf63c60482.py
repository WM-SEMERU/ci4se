def pause(self, length=None, **kwargs):
    return self.nest(Pause(length=length, **kwargs))