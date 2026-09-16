def register(self, mimetype):

    def dec(func):
        self._reg[mimetype] = func
        return func
    return dec