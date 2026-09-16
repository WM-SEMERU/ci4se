def roundness(self, value):
    if value is not None and not value in DG_V_ROUNDNESS:
        raise ValueError("Unrecognized value for roundness: '%s'" % value)
    self.__roundness = value