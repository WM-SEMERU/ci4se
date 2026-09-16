def activate(self, engine):
    LOGGER.debug("> Activating '{0}' Component.".format(self.__class__.
        __name__))
    self.__engine = engine
    self.__settings = self.__engine.settings
    self.__settings_section = self.name
    self.__preferences_manager = self.__engine.components_manager[
        'factory.preferences_manager']
    self.__tcp_server = TCPServer(self.__address, self.__port,
        RequestsStackDataHandler)
    self.activated = True
    return True