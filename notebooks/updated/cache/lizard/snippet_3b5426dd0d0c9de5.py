def set_default_preferences(self):
    LOGGER.debug('> Initializing default settings!')
    for key in self.__default_settings.allKeys():
        self.__settings.setValue(key, self.__default_settings.value(key))
    self.set_default_layouts()
    return True