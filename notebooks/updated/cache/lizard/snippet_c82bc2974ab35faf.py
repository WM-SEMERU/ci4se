def manner(self, value):
    if value is not None and not value in DG_C_MANNER:
        raise ValueError("Unrecognized value for manner: '%s'" % value)
    self.__manner = value