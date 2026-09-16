def FieldName(self, name):
    name = self.__StripName(name)
    if self.__name_convention == 'LOWER_CAMEL':
        name = Names.__ToLowerCamel(name)
    elif self.__name_convention == 'LOWER_WITH_UNDER':
        name = Names.__FromCamel(name)
    return Names.CleanName(name)