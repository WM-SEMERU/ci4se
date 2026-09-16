def require(self, value):
    if value is not None:
        assert type(value) in (tuple, list
            ), "'{0}' attribute: '{1}' type is not 'tuple' or 'list'!".format(
            'require', value)
    self.__require = value