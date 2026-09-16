def vertical_padding(self, value):
    if value is not None:
        assert type(value
            ) is int, "'{0}' attribute: '{1}' type is not 'int'!".format(
            'vertical_padding', value)
        assert value > 0, "'{0}' attribute: '{1}' need to be positive!".format(
            'vertical_padding', value)
    self.__vertical_padding = value