def get_value(self, attribute, section, default=''):
    if not self.attribute_exists(attribute, section):
        return default
    if attribute in self.__sections[section]:
        value = self.__sections[section][attribute]
    elif foundations.namespace.set_namespace(section, attribute
        ) in self.__sections[section]:
        value = self.__sections[section][foundations.namespace.
            set_namespace(section, attribute)]
    LOGGER.debug("> Attribute: '{0}', value: '{1}'.".format(attribute, value))
    return value