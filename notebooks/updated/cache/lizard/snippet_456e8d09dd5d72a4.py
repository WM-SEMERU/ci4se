def copy(self):
    cpy = type(self)()
    cpy._encoders = copy.copy(self._encoders)
    cpy._decoders = copy.copy(self._decoders)
    return cpy