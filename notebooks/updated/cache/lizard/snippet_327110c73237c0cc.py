def representation(self, mediatype):

    def wrapper(func):
        self.representations[mediatype] = func
        return func
    return wrapper