def post_input_accelerators(self, value):
    if value is not None:
        assert type(value) in (tuple, list
            ), "'{0}' attribute: '{1}' type is not 'tuple' or 'list'!".format(
            'post_input_accelerators', value)
    self.__post_input_accelerators = value