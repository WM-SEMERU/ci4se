def file_command(self, value):
    if value is not None:
        assert type(value
            ) is unicode, "'{0}' attribute: '{1}' type is not 'unicode'!".format(
            'file_command', value)
    self.__file_command = value