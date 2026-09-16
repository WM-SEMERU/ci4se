def validate_options(self, k, v):
    super().validate_options(k, v)
    if k == 'mode' and v not in MODE:
        raise ValueError("{}: '{}' is not a valid value for '{}'".format(
            self.__class__.__name, v, k))