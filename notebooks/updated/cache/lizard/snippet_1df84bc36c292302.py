def message(self):
    message = self.message_methods[self.session.method]()
    _LOGGER.debug(message)
    return message