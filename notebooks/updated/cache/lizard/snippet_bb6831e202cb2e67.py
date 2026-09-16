def remove_completer(self):
    if self.__completer:
        LOGGER.debug("> Removing '{0}' completer.".format(self.__completer))
        self.__completer.activated.disconnect(self.__insert_completion)
        self.__completer.deleteLater()
        self.__completer = None
    return True