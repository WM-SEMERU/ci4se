def comment_marker(self, value):
    if value is not None:
        assert type(value
            ) is unicode, "'{0}' attribute: '{1}' type is not 'unicode'!".format(
            'comment_marker', value)
    self.__comment_marker = value