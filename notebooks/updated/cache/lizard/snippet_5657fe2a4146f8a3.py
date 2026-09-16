def validate_options(self, k, v):
    super().validate_options(k, v)
    if k == 'delimiters':
        for d in v:
            if not isinstance(d, (dict, OrderedDict)):
                raise ValueError(
                    "{}: 'delimters' entries must be of dict type.".format(
                    self.__class__.__name__))
            for key, value in d.items():
                if key not in ('open', 'close', 'content'):
                    raise KeyError(
                        "{}: '{}' is not a valid key for a 'delimeters' entry."
                        .format(self.__class__.__name__, key))
                if not isinstance(value, str):
                    raise ValueError(
                        "{}: 'delimeters' '{}' key should have str values."
                        .format(self.__class__.__name__, value))