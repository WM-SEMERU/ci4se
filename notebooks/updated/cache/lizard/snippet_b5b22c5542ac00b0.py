def filters_in_format(self, value):
    if value is not None:
        assert type(value
            ) is unicode, "'{0}' attribute: '{1}' type is not 'unicode'!".format(
            'filters_in_format', value)
        assert os.path.exists(value
            ), "'{0}' attribute: '{1}' file doesn't exists!".format(
            'filters_in_format', value)
    self.__filters_in_format = value