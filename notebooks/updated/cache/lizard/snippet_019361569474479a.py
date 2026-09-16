def join(self, iterable):
    return self.__class__(super(ColorStr, self).join(iterable), keep_tags=True)