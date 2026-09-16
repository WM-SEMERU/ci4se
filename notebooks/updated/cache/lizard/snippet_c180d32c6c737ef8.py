def settings(self, value):
    if value is not None:
        assert type(value
            ) is dict, "'{0}' attribute: '{1}' type is not 'dict'!".format(
            'settings', value)
    self.__settings = foundations.data_structures.Structure(**{
        'case_sensitive': False, 'whole_word': False, 'regular_expressions':
        False})
    self.__settings.update(value)