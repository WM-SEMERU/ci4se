def auto_update(cls, function):

    def wrapper(self, *args, **kwargs):
        f = function(self, *args, **kwargs)
        self.update()
        return f
    return wrapper