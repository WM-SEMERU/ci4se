def send(self, message):
    message.update(self._globalFields)
    errors = []
    for dest in self._destinations:
        try:
            dest(message)
        except:
            errors.append(sys.exc_info())
    if errors:
        raise _DestinationsSendError(errors)