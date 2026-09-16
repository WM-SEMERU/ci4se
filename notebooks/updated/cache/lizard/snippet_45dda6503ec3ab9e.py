def update(self, **kwargs):
    self.__init__(self.callback, **dict(self.__original_kwargs__, **kwargs))