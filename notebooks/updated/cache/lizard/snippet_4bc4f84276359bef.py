def targets_format(self, value):
    if value is not None:
        assert type(value
            ) is unicode, "'{0}' attribute: '{1}' type is not 'unicode'!".format(
            'targets_format', value)
        assert os.path.exists(value
            ), "'{0}' attribute: '{1}' file doesn't exists!".format(
            'targets_format', value)
    self.__targets_format = value