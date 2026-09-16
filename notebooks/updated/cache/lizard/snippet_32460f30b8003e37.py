def Val(self, val, **kwargs):
    f = utils.lift(lambda z: val)
    return self.__then__(f, **kwargs)